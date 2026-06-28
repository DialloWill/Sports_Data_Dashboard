import requests
from datetime import datetime
from services.utils import is_cache_valid
from config import RAPIDAPI_KEY

# ── Cache ──────────────────────────────────────────────────────────────────────
_fights_cache = {"data": None, "timestamp": None}
_rankings_cache = {"data": None, "timestamp": None}

HEADERS = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "boxing-data-api.p.rapidapi.com"
}

BASE_URL = "https://boxing-data-api.p.rapidapi.com/v2"


def get_upcoming_fights():
    """Fetch upcoming and recent fights from the Boxing Data API."""
    if is_cache_valid(_fights_cache):
        return _fights_cache["data"]

    try:
        response = requests.get(
            f"{BASE_URL}/fights",
            headers=HEADERS,
            timeout=10
        )
        response.raise_for_status()
        raw = response.json()

        fights = []
        for fight in raw.get("data", []):
            fights.append({
                "title": fight.get("title", "TBD"),
                "date": fight.get("date", ""),
                "venue": fight.get("venue", ""),
                "location": fight.get("location", ""),
                "status": fight.get("status", ""),
                "card": fight.get("card_billing", ""),
                "division": fight.get("division", {}).get("name", ""),
                "fighter_1": fight.get("fighters", {}).get("fighter_1", {}).get("full_name", "TBD"),
                "fighter_2": fight.get("fighters", {}).get("fighter_2", {}).get("full_name", "TBD"),
                "winner": _get_winner(fight),
                "event": fight.get("event", {}).get("title", ""),
            })

        _fights_cache["data"] = fights
        _fights_cache["timestamp"] = datetime.now()
        return fights

    except Exception as e:
        print(f"Boxing fights error: {e}")
        return []


def get_rankings():
    """Fetch boxing rankings by division."""
    if is_cache_valid(_rankings_cache):
        return _rankings_cache["data"]

    try:
        response = requests.get(
            f"{BASE_URL}/rankings",
            headers=HEADERS,
            timeout=10
        )
        response.raise_for_status()
        raw = response.json()

        rankings = {}
        for entry in raw.get("data", []):
            division = entry.get("division", {}).get("name", "Unknown")
            if division not in rankings:
                rankings[division] = []
            rankings[division].append({
                "rank": entry.get("rank", ""),
                "fighter": entry.get("fighter", {}).get("full_name", "TBD"),
                "record": _format_record(entry.get("fighter", {})),
                "status": entry.get("status", ""),
            })

        _rankings_cache["data"] = rankings
        _rankings_cache["timestamp"] = datetime.now()
        return rankings

    except Exception as e:
        print(f"Boxing rankings error: {e}")
        return {}


def _get_winner(fight):
    """Extract winner name from fight data if available."""
    fighters = fight.get("fighters", {})
    for key in ["fighter_1", "fighter_2"]:
        f = fighters.get(key, {})
        if f.get("winner"):
            return f.get("full_name", "")
    return None


def _format_record(fighter):
    """Format fighter record as W-L-D."""
    w = fighter.get("wins", "")
    l = fighter.get("losses", "")
    d = fighter.get("draws", "")
    if w == "" and l == "" and d == "":
        return ""
    return f"{w}-{l}-{d}"