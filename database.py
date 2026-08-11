# database.py
# Handles all SQLite operations for user accounts.
# Uses sqlite3 (built into Python — no install needed).

import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

DB_PATH = "users.db"


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row   # rows behave like dicts
    return conn


def create_tables():
    """Run once at startup to create the users table."""
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            username   TEXT NOT NULL UNIQUE,
            email      TEXT NOT NULL UNIQUE,
            password   TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()


def create_user(username, email, password):
    """Register a new user. Returns (True, None) or (False, error_message)."""
    try:
        conn = get_db()
        hashed = generate_password_hash(password)
        conn.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, email, hashed)
        )
        conn.commit()
        conn.close()
        return True, None
    except sqlite3.IntegrityError as e:
        if "username" in str(e):
            return False, "Username already taken"
        if "email" in str(e):
            return False, "Email already registered"
        return False, "Registration failed"


def get_user_by_email(email):
    """Fetch user row by email."""
    conn = get_db()
    user = conn.execute(
        "SELECT * FROM users WHERE email = ?", (email,)
    ).fetchone()
    conn.close()
    return user


def verify_password(user, password):
    """Check plain password against stored hash."""
    return check_password_hash(user["password"], password)