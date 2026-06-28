import requests
from datetime import datetime
from services.utils import is_cache_valid

_cache = {
    "data": None,
    "timestamp": None
}

def get_mlb_standings():
    if is_cache_valid(_cache):
        return _cache["data"]

    url = "https://statsapi.mlb.com/api/v1/standings"
    params = {
        "leagueId": "103,104",
        "season": "2025",
        "standingsTypes": "regularSeason"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

    data = response.json()
    result = {"AL": [], "NL": []}

    for record in data["records"]:
        division_id = record["division"]["id"]
        # AL division IDs: 200, 201, 202 — everything else is NL
        league = "AL" if division_id in [200, 201, 202] else "NL"
        for team_record in record["teamRecords"]:
            result[league].append({
                "team": team_record["team"]["name"],
                "wins": team_record["wins"],
                "losses": team_record["losses"],
                "win_pct": team_record["winningPercentage"]
            })

    result["AL"] = sorted(result["AL"], key=lambda x: float(x["win_pct"]), reverse=True)
    result["NL"] = sorted(result["NL"], key=lambda x: float(x["win_pct"]), reverse=True)

    _cache["data"] = result
    _cache["timestamp"] = datetime.now()

    return result