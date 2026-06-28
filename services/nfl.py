import requests
from datetime import datetime
from services.utils import is_cache_valid

_cache = {
    "data": None,
    "timestamp": None
}

def get_nfl_standings():
    if is_cache_valid(_cache):
        return _cache["data"]

    url = "https://site.api.espn.com/apis/v2/sports/football/nfl/standings"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

    data = response.json()
    result = {"AFC": [], "NFC": []}

    for conference in data["children"]:
        conf_name = conference["abbreviation"]
        for entry in conference["standings"]["entries"]:
            team_name = entry["team"]["displayName"]
            # Build a flat dict of stat name → display value for easy lookup
            stats = {s["name"]: s["displayValue"] for s in entry["stats"]}
            result[conf_name].append({
                "team": team_name,
                "wins": stats.get("wins", "0"),
                "losses": stats.get("losses", "0"),
                "win_pct": stats.get("winPercent", "0")
            })

    result["AFC"] = sorted(result["AFC"], key=lambda x: float(x["win_pct"]), reverse=True)
    result["NFC"] = sorted(result["NFC"], key=lambda x: float(x["win_pct"]), reverse=True)

    _cache["data"] = result
    _cache["timestamp"] = datetime.now()

    return result