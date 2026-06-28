from flask import Flask, render_template
from config import BALLDONTLIE_API_KEY
from services.nba import get_nba_standings
from services.nfl import get_nfl_standings
from services.mlb import get_mlb_standings
from services.soccer import get_world_cup_standings
from services.boxing import get_upcoming_fights, get_rankings

app = Flask(__name__)

@app.route("/")
def index():
    nba_standings = get_nba_standings()
    nfl_data = get_nfl_standings()
    mlb_data = get_mlb_standings()
    soccer_data = get_world_cup_standings()
    boxing_fights = get_upcoming_fights()
    boxing_rankings = get_rankings()
    return render_template(
        "index.html",
        nba_standings=nba_standings,
        nfl_data=nfl_data,
        mlb_data=mlb_data,
        soccer_data=soccer_data,
        boxing_fights=boxing_fights,
        boxing_rankings=boxing_rankings
    )

if __name__ == "__main__":
    app.run(debug=True)