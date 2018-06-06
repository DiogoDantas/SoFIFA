# -*- coding: utf-8 -*-
import scrapy
import json

class SofifaSpider(scrapy.Spider):
    name='sofifa_stats'

    def __init__(self):
        with open('data/players.json') as json_data:
            self.players = json.load(json_data)
        self.player_count = 1

    def start_requests(self):
        urls = [
        'https://sofifa.com/player/158023'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for player in response.css('.info'):
            player_info = player.xpath('//div[@class="info"]//span/text()').extract()
            player_url_photo = player.xpath('//div[@class="player"]//img/@data-src')[0].extract()
            player_info = [info for info in player_info if info != ' ']
            player_stats = player.xpath('//tr//td[@class="text-center"]/text()').re(r'[\w ]+')
            player_stats_values = player.xpath('//tr//td[@class="text-center"]//span/text()').extract()
            player_teams = player.xpath('//div[@class="teams"]//tr//td//ul//li//label/text()').extract()
            player_teams_values = player.xpath('//div[@class="teams"]//tr//td//ul//li/text()').re(r'\w+')

            #remove some atributes from player team and national team
            player_teams = player_teams[:8]
            player_teams_values = player_teams_values[:4]
            player_teams_values.extend(player.xpath('//div[@class="teams"]//tr//td//ul//li//span/text()').extract())
            player_teams_values = player_teams_values[:8]

            ###########################################################

            player_tags = player.xpath('//div[@class="player"]//div//a//mark/text()').extract()
            player_operation = player.xpath('//div[@class="operation"]//a/text()').re(r'\w+')
            player_operation_values = player.xpath('//div[@class="operation"]//a//span/text()').extract()
            player_skills = player.xpath('//div[@class="columns"]//div//div//ul/li/text()').re(r'[\w ]+')
            player_traits = player_skills[34:]
            player_skills = player_skills[:34]
            player_skills_values = player.xpath('//div[@class="columns"]//div//div//ul/li//span/text()').extract()

            # Age 30 (Jun 24, 1987) 170cm 72kg'
            _, age, month, day, year, height, weight = player_info[-1].split()
            month = month.replace('(', '')
            day = int(day.replace(',', ''))
            year = int(year.replace(')', ''))
            height = int(height.replace('cm', ''))
            weight = int(weight.replace('kg', ''))

            stats = {k:v for k, v in zip(player_stats, player_stats_values)}
            stats["Overall Rating"] = int(stats["Overall Rating"])
            stats["Potential"] = int(stats["Potential"])

            #
            extra = {k:v for k, v in zip(player_teams, player_teams_values)}
            extra["International Reputation"] = int(extra["International Reputation"])
            extra["Weak Foot"] = int(extra["Weak Foot"])
            extra["Skill Moves"] = int(extra["Skill Moves"])

            player_info_dict = {
                    'name': player_info[0],
                    'photo_url': player_url_photo,
                    'positions': [position for position in player_info[1:] if position.isupper()],
                    'age': age,
                    'birth_date': '{}/{}/{}'.format(year, month, day),
                    'height': height,
                    'weight': weight,
                    'stats': stats,
            }
            player_skills_dict = {
                'player_hashtags': player_tags,
                    'player_operations': {k:v for k, v in zip(player_operation, player_operation_values)},
                    'player_skills':{
                        'attacking':{k.replace(' ', ''):int(v) for k, v in zip(player_skills[:5], player_skills_values[:5])},
                        'skill': {k.replace(' ', ''):int(v) for k, v in zip(player_skills[5:10], player_skills_values[5:10])},
                        'movement':{k.replace(' ', ''):int(v) for k, v in zip(player_skills[10:15], player_skills_values[10:15])},
                        'power': {k.replace(' ', ''):int(v) for k, v in zip(player_skills[15:20], player_skills_values[15:20])},
                        'mentality': {k.replace(' ', ''):int(v) for k, v in zip(player_skills[20:26], player_skills_values[20:26])},
                        'defending': {k.replace(' ', ''):int(v) for k, v in zip(player_skills[26:29], player_skills_values[26:29])},
                        'goalkeeping': {k.replace(' ', ''):int(v) for k, v in zip(player_skills[29:], player_skills_values[29:])}
                    },
                    'player_traits': player_traits
            }

            player_info_dict.update(extra)
            player_info_dict.update(player_skills_dict)

            yield {
                'player_info': player_info_dict
            }

            if self.player_count < len(self.players):
                next_page_url = 'https://sofifa.com' + self.players[self.player_count]['player_url'] + '?units=mks'
                self.player_count += 1
                yield scrapy.Request(url=next_page_url, callback=self.parse)