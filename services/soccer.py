from datetime import datetime
from services.utils import is_cache_valid

_cache = {
    "data": None,
    "timestamp": None
}

def get_world_cup_standings():
    if is_cache_valid(_cache):
        return _cache["data"]

    result = {
        "Group A": [
            {"team": "Mexico", "p": 3, "w": 3, "d": 0, "l": 0, "gf": 6, "ga": 0, "gd": 6, "pts": 9},
            {"team": "South Africa", "p": 3, "w": 1, "d": 1, "l": 1, "gf": 2, "ga": 3, "gd": -1, "pts": 4},
            {"team": "Korea Republic", "p": 3, "w": 1, "d": 0, "l": 2, "gf": 2, "ga": 3, "gd": -1, "pts": 3},
            {"team": "Czechia", "p": 3, "w": 0, "d": 1, "l": 2, "gf": 2, "ga": 6, "gd": -4, "pts": 1},
        ],
        "Group B": [
            {"team": "Switzerland", "p": 3, "w": 2, "d": 1, "l": 0, "gf": 7, "ga": 3, "gd": 4, "pts": 7},
            {"team": "Canada", "p": 3, "w": 1, "d": 1, "l": 1, "gf": 8, "ga": 3, "gd": 5, "pts": 4},
            {"team": "Bosnia and Herzegovina", "p": 3, "w": 1, "d": 1, "l": 1, "gf": 5, "ga": 6, "gd": -1, "pts": 4},
            {"team": "Qatar", "p": 3, "w": 0, "d": 1, "l": 2, "gf": 2, "ga": 10, "gd": -8, "pts": 1},
        ],
        "Group C": [
            {"team": "Brazil", "p": 3, "w": 2, "d": 1, "l": 0, "gf": 7, "ga": 1, "gd": 6, "pts": 7},
            {"team": "Morocco", "p": 3, "w": 2, "d": 1, "l": 0, "gf": 6, "ga": 3, "gd": 3, "pts": 7},
            {"team": "Scotland", "p": 3, "w": 1, "d": 0, "l": 2, "gf": 1, "ga": 4, "gd": -3, "pts": 3},
            {"team": "Haiti", "p": 3, "w": 0, "d": 0, "l": 3, "gf": 2, "ga": 8, "gd": -6, "pts": 0},
        ],
        "Group D": [
            {"team": "USA", "p": 3, "w": 2, "d": 0, "l": 1, "gf": 8, "ga": 4, "gd": 4, "pts": 6},
            {"team": "Australia", "p": 3, "w": 1, "d": 1, "l": 1, "gf": 2, "ga": 2, "gd": 0, "pts": 4},
            {"team": "Paraguay", "p": 3, "w": 1, "d": 1, "l": 1, "gf": 2, "ga": 4, "gd": -2, "pts": 4},
            {"team": "Turkey", "p": 3, "w": 1, "d": 0, "l": 2, "gf": 3, "ga": 5, "gd": -2, "pts": 3},
        ],
        "Group E": [
            {"team": "Germany", "p": 3, "w": 2, "d": 0, "l": 1, "gf": 10, "ga": 4, "gd": 6, "pts": 6},
            {"team": "Côte d'Ivoire", "p": 3, "w": 2, "d": 0, "l": 1, "gf": 4, "ga": 2, "gd": 2, "pts": 6},
            {"team": "Ecuador", "p": 3, "w": 1, "d": 1, "l": 1, "gf": 2, "ga": 2, "gd": 0, "pts": 4},
            {"team": "Curaçao", "p": 3, "w": 0, "d": 1, "l": 2, "gf": 1, "ga": 9, "gd": -8, "pts": 1},
        ],
        "Group F": [
            {"team": "Netherlands", "p": 3, "w": 2, "d": 1, "l": 0, "gf": 10, "ga": 4, "gd": 6, "pts": 7},
            {"team": "Japan", "p": 3, "w": 1, "d": 2, "l": 0, "gf": 7, "ga": 3, "gd": 4, "pts": 5},
            {"team": "Sweden", "p": 3, "w": 1, "d": 1, "l": 1, "gf": 7, "ga": 7, "gd": 0, "pts": 4},
            {"team": "Tunisia", "p": 3, "w": 0, "d": 0, "l": 3, "gf": 2, "ga": 12, "gd": -10, "pts": 0},
        ],
        "Group G": [
            {"team": "Belgium", "p": 3, "w": 1, "d": 2, "l": 0, "gf": 6, "ga": 2, "gd": 4, "pts": 5},
            {"team": "Egypt", "p": 3, "w": 1, "d": 2, "l": 0, "gf": 5, "ga": 3, "gd": 2, "pts": 5},
            {"team": "IR Iran", "p": 3, "w": 0, "d": 3, "l": 0, "gf": 3, "ga": 3, "gd": 0, "pts": 3},
            {"team": "New Zealand", "p": 3, "w": 0, "d": 1, "l": 2, "gf": 4, "ga": 10, "gd": -6, "pts": 1},
        ],
        "Group H": [
            {"team": "Spain", "p": 3, "w": 2, "d": 1, "l": 0, "gf": 5, "ga": 0, "gd": 5, "pts": 7},
            {"team": "Cabo Verde", "p": 3, "w": 0, "d": 3, "l": 0, "gf": 2, "ga": 2, "gd": 0, "pts": 3},
            {"team": "Uruguay", "p": 3, "w": 0, "d": 2, "l": 1, "gf": 3, "ga": 4, "gd": -1, "pts": 2},
            {"team": "Saudi Arabia", "p": 3, "w": 0, "d": 2, "l": 1, "gf": 1, "ga": 5, "gd": -4, "pts": 2},
        ],
        "Group I": [
            {"team": "France", "p": 3, "w": 3, "d": 0, "l": 0, "gf": 10, "ga": 2, "gd": 8, "pts": 9},
            {"team": "Norway", "p": 3, "w": 2, "d": 0, "l": 1, "gf": 8, "ga": 7, "gd": 1, "pts": 6},
            {"team": "Senegal", "p": 3, "w": 1, "d": 0, "l": 2, "gf": 8, "ga": 6, "gd": 2, "pts": 3},
            {"team": "Iraq", "p": 3, "w": 0, "d": 0, "l": 3, "gf": 1, "ga": 12, "gd": -11, "pts": 0},
        ],
        "Group J": [
            {"team": "Argentina", "p": 3, "w": 3, "d": 0, "l": 0, "gf": 8, "ga": 1, "gd": 7, "pts": 9},
            {"team": "Austria", "p": 3, "w": 1, "d": 1, "l": 1, "gf": 6, "ga": 6, "gd": 0, "pts": 4},
            {"team": "Algeria", "p": 3, "w": 1, "d": 1, "l": 1, "gf": 5, "ga": 7, "gd": -2, "pts": 4},
            {"team": "Jordan", "p": 3, "w": 0, "d": 0, "l": 3, "gf": 3, "ga": 8, "gd": -5, "pts": 0},
        ],
        "Group K": [
            {"team": "Colombia", "p": 3, "w": 2, "d": 1, "l": 0, "gf": 4, "ga": 1, "gd": 3, "pts": 7},
            {"team": "Portugal", "p": 3, "w": 1, "d": 2, "l": 0, "gf": 6, "ga": 1, "gd": 5, "pts": 5},
            {"team": "Congo DR", "p": 3, "w": 1, "d": 1, "l": 1, "gf": 4, "ga": 3, "gd": 1, "pts": 4},
            {"team": "Uzbekistan", "p": 3, "w": 0, "d": 0, "l": 3, "gf": 2, "ga": 11, "gd": -9, "pts": 0},
        ],
        "Group L": [
            {"team": "England", "p": 3, "w": 2, "d": 1, "l": 0, "gf": 6, "ga": 2, "gd": 4, "pts": 7},
            {"team": "Croatia", "p": 3, "w": 2, "d": 0, "l": 1, "gf": 5, "ga": 5, "gd": 0, "pts": 6},
            {"team": "Ghana", "p": 3, "w": 1, "d": 1, "l": 1, "gf": 2, "ga": 2, "gd": 0, "pts": 4},
            {"team": "Panama", "p": 3, "w": 0, "d": 0, "l": 3, "gf": 0, "ga": 4, "gd": -4, "pts": 0},
        ],
    }

    _cache["data"] = result
    _cache["timestamp"] = datetime.now()

    return result