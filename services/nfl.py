import requests
from datetime import datetime
from services.utils import is_cache_valid
from config import RAPIDAPI_KEY

_cache = {
    "data": None,
    "timestamp": None
}

HEADERS = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "sport-highlights-api.p.rapidapi.com"
}

def get_nfl_standings():
    if is_cache_valid(_cache):
        return _cache["data"]

    url = "https://sport-highlights-api.p.rapidapi.com/american-football/standings"

    params = {
        "year": "2024",
        "leagueType": "NFL"
    }

    try:
        response = requests.get(url, headers=HEADERS, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

    data = response.json()
    result = {"AFC": [], "NFC": []}

    # API returns multiple seasons — filter to Regular Season only
    regular_season = None
    for season in data.get("data", []):
        if season.get("seasonType") == "Regular Season" and season.get("year") == 2024:
            regular_season = season
            break

    if not regular_season:
        return {"error": "No 2024 regular season data found"}

    conf_name = regular_season.get("abbreviation", "")
    if conf_name not in result:
        # API returns one conference per object — need to handle both AFC and NFC
        # so we loop through all season objects
        pass

    for season in data.get("data", []):
        if season.get("seasonType") != "Regular Season" or season.get("year") != 2024:
            continue

        conf_name = season.get("abbreviation", "")
        if conf_name not in result:
            continue

        for entry in season.get("data", []):
            team = entry.get("team", {})
            stats = {s["displayName"]: s["value"] for s in entry.get("statistics", [])}

            result[conf_name].append({
                "team": team.get("displayName", "Unknown"),
                "wins": stats.get("Wins", "0"),
                "losses": stats.get("Losses", "0"),
                "win_pct": stats.get("Win Percentage", "0")
            })

    # Sort by win percentage descending
    for conf in result:
        result[conf] = sorted(
            result[conf],
            key=lambda x: float(x["win_pct"]) if x["win_pct"] not in ("", "-") else 0.0,
            reverse=True
        )

    _cache["data"] = result
    _cache["timestamp"] = datetime.now()

    return result