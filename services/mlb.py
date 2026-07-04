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

def get_mlb_standings():
    if is_cache_valid(_cache):
        return _cache["data"]

    url = "https://sport-highlights-api.p.rapidapi.com/baseball/standings"

    params = {
        "year": "2025",
        "leagueType": "MLB"
    }

    try:
        response = requests.get(url, headers=HEADERS, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

    data = response.json()
    result = {"AL": [], "NL": []}

    for season in data.get("data", []):
        # Only process AL and NL regular season
        if season.get("seasonType") != "Regular Season" or season.get("year") != 2025:
            continue

        abbr = season.get("abbreviation", "")
        if abbr not in result:
            continue

        for entry in season.get("data", []):
            team_name = entry.get("name", "Unknown")
            # Stats use abbreviation as key
            stats = {s["abbreviation"]: s["displayValue"] for s in entry.get("stats", [])}

            wins = stats.get("W", "0")
            losses = stats.get("L", "0")
            win_pct = stats.get("PCT", "0")

            result[abbr].append({
                "team": team_name,
                "wins": wins,
                "losses": losses,
                "win_pct": win_pct
            })

        result[abbr] = sorted(
            result[abbr],
            key=lambda x: float(x["win_pct"].lstrip(".")) if x["win_pct"] not in ("", "-", "0") else 0.0,
            reverse=True
        )

    _cache["data"] = result
    _cache["timestamp"] = datetime.now()

    return result