# 2024-25 NBA Final Standings — hardcoded, season is complete
# Removed live API due to balldontlie.io free tier rate limiting on full season pagination

def get_nba_standings():
    return {
        "East": [
            {"team": "Cleveland Cavaliers",   "wins": 64, "losses": 18, "win_pct": ".780"},
            {"team": "Boston Celtics",         "wins": 61, "losses": 21, "win_pct": ".744"},
            {"team": "New York Knicks",        "wins": 51, "losses": 31, "win_pct": ".622"},
            {"team": "Indiana Pacers",         "wins": 50, "losses": 32, "win_pct": ".610"},
            {"team": "Milwaukee Bucks",        "wins": 48, "losses": 34, "win_pct": ".585"},
            {"team": "Detroit Pistons",        "wins": 44, "losses": 38, "win_pct": ".537"},
            {"team": "Orlando Magic",          "wins": 41, "losses": 41, "win_pct": ".500"},
            {"team": "Atlanta Hawks",          "wins": 40, "losses": 42, "win_pct": ".488"},
            {"team": "Chicago Bulls",          "wins": 39, "losses": 43, "win_pct": ".476"},
            {"team": "Miami Heat",             "wins": 37, "losses": 45, "win_pct": ".451"},
            {"team": "Toronto Raptors",        "wins": 30, "losses": 52, "win_pct": ".366"},
            {"team": "Brooklyn Nets",          "wins": 26, "losses": 56, "win_pct": ".317"},
            {"team": "Philadelphia 76ers",     "wins": 24, "losses": 58, "win_pct": ".293"},
            {"team": "Charlotte Hornets",      "wins": 19, "losses": 63, "win_pct": ".232"},
            {"team": "Washington Wizards",     "wins": 18, "losses": 64, "win_pct": ".220"},
        ],
        "West": [
            {"team": "Oklahoma City Thunder",  "wins": 68, "losses": 14, "win_pct": ".829"},
            {"team": "Houston Rockets",        "wins": 52, "losses": 30, "win_pct": ".634"},
            {"team": "Los Angeles Lakers",     "wins": 50, "losses": 32, "win_pct": ".610"},
            {"team": "Denver Nuggets",         "wins": 50, "losses": 32, "win_pct": ".610"},
            {"team": "Los Angeles Clippers",   "wins": 50, "losses": 32, "win_pct": ".610"},
            {"team": "Minnesota Timberwolves", "wins": 49, "losses": 33, "win_pct": ".598"},
            {"team": "Golden State Warriors",  "wins": 48, "losses": 34, "win_pct": ".585"},
            {"team": "Memphis Grizzlies",      "wins": 48, "losses": 34, "win_pct": ".585"},
            {"team": "Sacramento Kings",       "wins": 40, "losses": 42, "win_pct": ".488"},
            {"team": "Dallas Mavericks",       "wins": 39, "losses": 43, "win_pct": ".476"},
            {"team": "Phoenix Suns",           "wins": 36, "losses": 46, "win_pct": ".439"},
            {"team": "Portland Trail Blazers", "wins": 36, "losses": 46, "win_pct": ".439"},
            {"team": "San Antonio Spurs",      "wins": 34, "losses": 48, "win_pct": ".415"},
            {"team": "New Orleans Pelicans",   "wins": 21, "losses": 61, "win_pct": ".256"},
            {"team": "Utah Jazz",              "wins": 17, "losses": 65, "win_pct": ".207"},
        ]
    }

