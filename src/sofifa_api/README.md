##### Examples:

|    parameter   |           example          |
|:--------------:|:--------------------------:|
|      name      |         name=Neymar        |
|       age      |           age=20           |
|    positions   | positions=CAM&positions=CM |
| overall_rating |      overall_rating=90     |
|    potential   |        potential=90        |

> http://sofifa-api.herokuapp.com/api/v1/players/?name=Neymar
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "5b31d573831e1a0008c0f805",
            "name": "Neymar da Silva Santos Jr.",
            "photo_url": "https://cdn.sofifa.org/1x/18/players/190871.png",
            "positions": [
                "LW"
            ],
            "age": "25",
            "birth_date": "1992/Feb/5",
            "height": 175,
            "weight": 68,
            "overall_rating": 92,
            "potential": 93,
            "value": "€119.5M",
            "wage": "€280K",
            "preferred_foot": "Right",
            "international_reputation": 5,
            "weak_foot": 5,
            "skill_moves": 5,
            "work_rate": "High / Medium",
            "body_type": "Neymar",
            "real_face": "Yes",
            "release_clause": "€230M",
            "player_hashtags": [
                "#Speedster",
                "#Dribbler",
                "#Acrobat"
            ],
            "player_traits": [
                "Diver",
                "Flair",
                "Speed Dribbler",
                "Technical Dribbler",
                "Takes Finesse Free Kicks"
            ],
            "social": {
                "follow": 1307,
                "like": 434,
                "dislike": 74
            },
            "skills": {
                "crossing": 75,
                "finishing": 88,
                "heading_accuracy": 62,
                "short_passing": 82,
                "volleys": 83,
                "dribbling": 96,
                "curve": 82,
                "fk_accuracy": 84,
                "long_passing": 75,
                "ball_control": 95,
                "acceleration": 94,
                "sprint_speed": 90,
                "agility": 96,
                "reactions": 88,
                "balance": 82,
                "shot_power": 80,
                "jumping": 61,
                "stamina": 78,
                "strength": 53,
                "long_shots": 78,
                "aggression": 56,
                "interceptions": 36,
                "positioning": 90,
                "vision": 83,
                "penalties": 81,
                "composure": 92,
                "marking": 21,
                "standing_tackle": 24,
                "sliding_tackle": 33,
                "gk_diving": 9,
                "gk_handling": 9,
                "gk_kicking": 15,
                "gk_positioning": 15,
                "gk_reflexes": 11
            }
        }
    ]
}
```
