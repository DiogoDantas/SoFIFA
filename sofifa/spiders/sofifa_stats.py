import scrapy

class SofifaSpider(scrapy.Spider):
    name='sofifa_stats'

    def start_requests(self):
        urls = [
        'https://sofifa.com/player/158023'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for player in response.css('.info'):
            player_info = player.xpath('//div[@class="info"]//span/text()').extract()
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

            yield {
                'player_info': {
                    'name': player_info[0],
                    'positions': [position for position in player_info[1:] if position.isupper()],
                    'age': age,
                    'birth_date': '{}/{}/{}'.format(year, month, day),
                    'height': height,
                    'weight': weight,
                    'stats': stats,
                    'extra_info': {k:v for k, v in zip(player_teams, player_teams_values)}
                    
                },
            }

            print(player_info)
            print(player_stats)
            print(player_stats_values)
            print(player_teams)
            print(player_teams_values)
            print(player_tags)
            print(player_operation)
            print(player_operation_values)
            print(player_skills)
            print(player_skills_values)
            print(player_traits)
            
            
            
            
            
            
            