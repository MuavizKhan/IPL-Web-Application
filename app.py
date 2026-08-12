# app.py — IPL Web App
# Calls the API Service for all data.
# Handles auth via Flask sessions + SQLite.

import os
from functools import wraps
import requests
from flask import Flask, render_template, request, session, redirect, flash
import database

app = Flask(__name__)

# ── Read from environment variables in production, fallback for local dev
app.secret_key = os.environ.get("SECRET_KEY", "ipl-local-dev-key")
API_BASE       = os.environ.get("API_BASE", "http://127.0.0.1:5000/api/v1")


# ── Helpers ────────────────────────────────────────────────────────────

def login_required(f):
    """Decorator — blocks any route if user is not logged in."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in to access this page.", "error")
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated


def api_get(endpoint, params=None):
    try:
        r = requests.get(
            f"{API_BASE}{endpoint}",
            params=params,
            timeout=120
        )
        body = r.json()
        if body.get("status") == "success":
            return body["data"], None
        return None, body.get("message", "Something went wrong")

    except requests.exceptions.Timeout:
        return None, "The server is waking up — please try again in 30 seconds."

    except requests.exceptions.ConnectionError:
        return None, "Could not connect to the API. Please try again shortly."

    except Exception as e:
        return None, "Something went wrong. Please try again."

def get_teams():
    """Fetch all team names — used by multiple pages."""
    data, _ = api_get("/teams")
    return data["teams"] if data else []


# ── Auth Routes ────────────────────────────────────────────────────────

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if "user_id" in session:
        return redirect("/dashboard")
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email    = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        confirm  = request.form.get("confirm", "")

        if not all([username, email, password, confirm]):
            flash("All fields are required.", "error")
        elif password != confirm:
            flash("Passwords do not match.", "error")
        elif len(password) < 6:
            flash("Password must be at least 6 characters.", "error")
        else:
            ok, err = database.create_user(username, email, password)
            if ok:
                flash("Account created! Please log in.", "success")
                return redirect("/login")
            else:
                flash(err, "error")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user_id" in session:
        return redirect("/dashboard")
    if request.method == "POST":
        email    = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        user = database.get_user_by_email(email)
        if user and database.verify_password(user, password):
            session["user_id"]  = user["id"]
            session["username"] = user["username"]
            flash(f"Welcome back, {user['username']}!", "success")
            return redirect("/dashboard")
        else:
            flash("Invalid email or password.", "error")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect("/")


# ── Protected Pages ────────────────────────────────────────────────────

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")


@app.route("/team")
@login_required
def team():
    teams = get_teams()
    team1  = request.args.get("team1")
    team2  = request.args.get("team2")
    result = None
    error  = None

    if team1 and team2:
        result, error = api_get("/teamvteam", {"team1": team1, "team2": team2})

    return render_template("team.html", teams=teams, result=result,
                           error=error, team1=team1, team2=team2)


@app.route("/team-record")
@login_required
def team_record():
    teams  = get_teams()
    team   = request.args.get("team")
    result = None
    error  = None

    if team:
        result, error = api_get("/team-record", {"team": team})

    return render_template("team_record.html", teams=teams,
                           result=result, error=error, selected=team)


@app.route("/batsman")
@login_required
def batsman():
    name   = request.args.get("batsman", "").strip()
    result = None
    error  = None

    if name:
        result, error = api_get("/batting-record", {"batsman": name})

    return render_template("batsman.html", result=result,
                           error=error, name=name)


@app.route("/bowler")
@login_required
def bowler():
    name   = request.args.get("bowler", "").strip()
    result = None
    error  = None

    if name:
        result, error = api_get("/bowling-record", {"bowler": name})

    return render_template("bowler.html", result=result,
                           error=error, name=name)


@app.route("/leaderboard")
@login_required
def leaderboard():
    season   = request.args.get("season", "")
    bat_data, _ = api_get("/batting-leaderboard",
                          {"season": season, "top": 10} if season else {"top": 10})
    bowl_data, _ = api_get("/bowling-leaderboard",
                           {"season": season, "top": 10} if season else {"top": 10})
    return render_template("leaderboard.html", bat=bat_data,
                           bowl=bowl_data, season=season)


@app.route("/h2h")
@login_required
def h2h():
    batsman = request.args.get("batsman", "").strip()
    bowler  = request.args.get("bowler", "").strip()
    result  = None
    error   = None

    if batsman and bowler:
        result, error = api_get("/player-h2h",
                                {"batsman": batsman, "bowler": bowler})

    return render_template("h2h.html", result=result, error=error,
                           batsman=batsman, bowler=bowler)


@app.route("/impact")
@login_required
def impact():
    name   = request.args.get("player", "").strip()
    result = None
    error  = None

    if name:
        result, error = api_get("/impact", {"player": name})

    return render_template("impact.html", result=result,
                           error=error, name=name)


@app.route("/predict")
@login_required
def predict():
    teams  = get_teams()
    team1  = request.args.get("team1", "")
    team2  = request.args.get("team2", "")
    venue  = request.args.get("venue", "")
    result = None
    error  = None

    if team1 and team2:
        result, error = api_get("/predict",
                                {"team1": team1, "team2": team2, "venue": venue})

    return render_template("predict.html", teams=teams, result=result,
                           error=error, team1=team1, team2=team2, venue=venue)


# ── Run ────────────────────────────────────────────────────────────────

database.create_tables()  

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7000))
    app.run(debug=False, host="0.0.0.0", port=port)