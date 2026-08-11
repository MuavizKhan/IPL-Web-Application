# 🏏 IPL Analytics Web App

**A full-stack web application for exploring IPL cricket statistics. Create an account, log in, and access batting records, bowling stats, head-to-head comparisons, impact scores, and match predictions.**

Built on top of the https://github.com/MuavizKhan/IPL-API-Service.

---

## 🌐 Live App

```
https://ipl-web-application.onrender.com
```

## 🤔 What Is This?

This is a **web application** — meaning you open it in a browser, create an account, and use it like a regular website. No technical knowledge needed.

It connects to the IPL Analytics API behind the scenes and presents the data in a clean, readable interface.

**Who is this for?**
- Cricket fans who want to look up IPL stats
- Developers who want to see how the API is used in a real app
- Anyone curious about IPL data

---

## 🚀 How to Use (Complete Guide — No Tech Knowledge Needed)

### Step 1 — Open the app
Go to `https://ipl-web-application.onrender.com` in any browser (Chrome, Firefox, Safari, Edge).

### Step 2 — Create a free account
- Click **Get Started**
- Enter your name, email address, and a password
- Click **Register**

### Step 3 — Log in
- Click **Log In**
- Enter your email and password
- Click **Log In**

### Step 4 — You're on the Dashboard
You'll see 8 feature cards. Click any card to explore.

---

## 🎯 Features — What Each Page Does

---

### 🏏 Batsman Record
**What it shows:** Career statistics for any IPL batsman.

**How to use:**
1. Click **Batsman Record** on the dashboard
2. Type a player's name in the search box
3. Click **Search**

**What you'll see:**
- Total runs, innings, batting average, strike rate
- Number of 50s and 100s, highest score
- Total fours and sixes hit
- Boundary percentage (how much of their runs come from boundaries)
- Man of the Match awards won
- A full table showing how they perform against each IPL team

**Player name format to use:**
```
V Kohli          (not Virat Kohli)
RG Sharma        (not Rohit Sharma)
AB de Villiers
MS Dhoni
SR Watson
DA Warner
```

---

### 🎯 Bowler Record
**What it shows:** Career statistics for any IPL bowler.

**How to use:**
1. Click **Bowler Record**
2. Type a player's name
3. Click **Search**

**What you'll see:**
- Total wickets, innings bowled, economy rate
- Bowling average (runs per wicket)
- Best bowling figures (e.g. 5/10 means 5 wickets for 10 runs)
- Number of 3-wicket and 5-wicket hauls
- Dot ball percentage (how often they bowl a dot ball)
- Man of the Match awards
- How they perform against each team

**Player name format to use:**
```
JJ Bumrah
SL Malinga
Harbhajan Singh
B Kumar
```

---

### 🆚 Team vs Team
**What it shows:** Head-to-head record between any two IPL teams.

**How to use:**
1. Click **Team vs Team**
2. Select Team 1 from the dropdown
3. Select Team 2 from the dropdown
4. Click **Compare**

**What you'll see:**
- Total matches played between the two teams
- How many each team has won
- Last 5 match results

---

### 🏆 Team Record
**What it shows:** A single team's complete record — overall and against each opponent.

**How to use:**
1. Click **Team Record**
2. Select a team from the dropdown
3. Click **View Record**

**What you'll see:**
- Total matches played, won, lost, no result
- Win percentage
- Number of IPL titles won
- Full breakdown of their record against every other team

---

### 📊 Leaderboard
**What it shows:** Top 10 run-scorers and top 10 wicket-takers.

**How to use:**
1. Click **Leaderboard**
2. Optionally type a year (e.g. `2023`) to filter by season
3. Click **Filter** (or **All Time** to see the all-time records)

**What you'll see:**
- Top 10 batsmen: ranked by runs, with innings count, average, strike rate
- Top 10 bowlers: ranked by wickets, with innings count, economy, average

---

### ⚡ Player H2H (Head to Head)
**What it shows:** The exact record of one batsman facing one specific bowler — using ball-by-ball data.

This is the most unique feature. No cricket website gives you this level of detail.

**How to use:**
1. Click **Player H2H**
2. Enter a batsman's name
3. Enter a bowler's name
4. Click **Find H2H**

**What you'll see:**
- Total balls the batsman has faced from this bowler
- Total runs scored in those balls
- How many times they were dismissed
- Strike rate against this bowler
- Dot ball percentage
- Fours and sixes hit
- How they were dismissed (caught, bowled, lbw, etc.)

**Example to try:** Batsman = `V Kohli`, Bowler = `JJ Bumrah`

---

### 💥 Impact Score
**What it shows:** A custom-built player rating. Scores any player between 0–100 and gives them a tier.

**How to use:**
1. Click **Impact Score**
2. Type any player's name
3. Click **Calculate**

**What you'll see:**
- An Impact Score between 0–100
- A tier: Elite / Impact Player / Decent / Developing
- Score breakdown showing which factors contributed

**Tier guide:**
| Score | Tier | Meaning |
|-------|------|---------|
| 80–100 | 🥇 Elite | Among the best in IPL history |
| 60–79 | 🥈 Impact Player | Consistently match-winning |
| 40–59 | 🥉 Decent | Solid contributor |
| 0–39 | 📈 Developing | Still developing their IPL game |

---

### 🔮 Match Predictor
**What it shows:** Rule-based win probability for a match between two teams.

**How to use:**
1. Click **Match Predictor**
2. Select Team 1 from the dropdown
3. Select Team 2 from the dropdown
4. Optionally type a venue name
5. Click **Predict**

**What you'll see:**
- A horizontal bar showing win probability for each team
- Predicted winner
- Confidence level (Low / Medium / High)
- Key reasons behind the prediction

**Example:** Team1 = `Mumbai Indians`, Team2 = `Chennai Super Kings`, Venue = `Wankhede`

> **Important:** This is a statistical prediction based on historical data. It is not a guarantee of who will win.

---

## 🔐 Account & Privacy

- Your password is **never stored in plain text** — it's hashed using industry-standard encryption
- You need an account to access any data pages (the dashboard, stats pages, etc.)
- Guests can only see the home page, login, and register pages
- Click **Logout** in the top navigation to end your session

---

## 🛠️ Tech Stack

| Component | Technology | What it does |
|-----------|-----------|-------------|
| Language | Python 3.10+ | Core language |
| Web Framework | Flask | Handles routing and requests |
| Templates | Jinja2 | Renders HTML pages |
| Auth | Werkzeug | Hashes and verifies passwords |
| User Database | SQLite | Stores user accounts locally |
| Styling | Custom CSS | All page styling |
| Data | IPL Analytics API | All cricket stats come from here |
| Production Server | Gunicorn | Runs Flask in production |
| Deployment | Render | Free cloud hosting |

---

## 🏗️ How It Works

```
You (Browser)
     │
     │  You visit a page, fill a form, click a button
     ▼
IPL Web App
┌──────────────────────────────────────────────┐
│                                              │
│  app.py           ← Handles all pages        │
│  database.py      ← Manages user accounts    │
│  templates/       ← 13 HTML page templates   │
│  static/style.css ← All styling              │
│                                              │
└──────────────────────────────────────────────┘
     │
     │  Web app asks the API for cricket data
     ▼
IPL Analytics API  (separate service)
┌──────────────────────────────────────────────┐
│  Processes 200,000+ ball-by-ball deliveries  │
│  Returns clean JSON data                     │
└──────────────────────────────────────────────┘
     │
     │  API fetches data from
     ▼
Google Sheets  (Kaggle IPL Dataset)
```

The web app itself does not store any cricket data. It just asks the API, gets the data, and displays it for you.

---

## 📂 Project Structure

```
IPL-Web-App/
│
├── app.py                  ← All routes and auth logic
├── database.py             ← User registration and login
│
├── templates/              ← One HTML file per page
│   ├── base.html           ← Shared navbar + header
│   ├── home.html           ← Landing page
│   ├── login.html          ← Login form
│   ├── register.html       ← Registration form
│   ├── dashboard.html      ← 8 feature cards
│   ├── batsman.html        ← Batsman stats page
│   ├── bowler.html         ← Bowler stats page
│   ├── team.html           ← Team vs team
│   ├── team_record.html    ← Single team record
│   ├── leaderboard.html    ← Top performers
│   ├── h2h.html            ← Player head to head
│   ├── impact.html         ← Impact score
│   └── predict.html        ← Match predictor
│
├── static/
│   └── style.css           ← All page styling
│
├── requirements.txt        ← Python packages needed
├── .gitignore
└── README.md
```

---

## 🚀 Run Locally (For Developers)

> The **IPL API Service must be running first** on port 5000 before you run the web app.

```bash
# Step 1 — Start the API service first (in a separate terminal)
cd ipl-api-service
python app.py
# API now running at http://127.0.0.1:5000

# Step 2 — In a NEW terminal, clone and run the web app
git https://github.com/MuavizKhan/IPL-Web-Application
cd ipl-web-app

# Step 3 — Create virtual environment
python -m venv .venv

# Activate:
.venv\Scripts\activate          # Windows
source .venv/bin/activate        # Mac / Linux

# Step 4 — Install dependencies
pip install -r requirements.txt

# Step 5 — Run
python app.py

# Web App is live at: http://127.0.0.1:7000
```

---

> ⚠️ **Known limitation (free tier):** User accounts are stored in SQLite, which resets when Render restarts the service (happens after 15 minutes of inactivity). If your account disappears, just register again. In a production app this would be fixed by using PostgreSQL.

---

## 🔮 Future Improvements

- **PostgreSQL** — Persistent user accounts that survive server restarts
- **User profile page** — See your search history
- **Player comparison** — Compare two players side by side
- **Visualisations** — Add charts and graphs for stats
- **Player autocomplete** — Suggest names as you type
- **Season filter on all pages** — Filter any stat by year
- **Mobile app** — Use the API to build a mobile version

---

## 👤 Author

Built by **Muaviz Maroof Khan**

- 🔌 API: https://github.com/MuavizKhan/IPL-API-Service
