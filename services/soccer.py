import requests
from datetime import datetime
from services.utils import is_cache_valid

_cache = {
    "data": None,
    "timestamp": None
}

def get_world_cup_standings():
    if is_cache_valid(_cache):
        return _cache["data"]

    url = "https://wcup2026.org/api/data.php"
    params = {"action": "standings"}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

    data = response.json()

    if not data.get("ok"):
        return {"error": "API returned an error"}

    result = {}

    for group_name, teams in data["standings"].items():
        # Sort by FIFA tiebreaker rules: points → goal difference → goals scored
        result[group_name] = sorted(
            teams,
            key=lambda x: (x["pts"], x["gd"], x["gf"]),
            reverse=True
        )

    _cache["data"] = result
    _cache["timestamp"] = datetime.now()

    return result