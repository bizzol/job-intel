# db.py
# Mike Bell
# 05/21/2026

import sqlite3
from pathlib import Path

DB_PATH = Path("jobs.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            url TEXT UNIQUE,
            source TEXT,
            date_posted TEXT,
            discovered_at TEXT,
            score INTEGER,
            description TEXT
        )
        """
    )

    conn.commit()
    conn.close()

def insert_job(job):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO jobs
            (
                title,
                company,
                location,
                url,
                source,
                date_posted,
                discovered_at,
                score,
                description
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                job["title"],
                job["company"],
                job["location"],
                job["url"],
                job["source"],
                job["date_posted"],
                job["discovered_at"],
                job["score"],
                job["description"]
            )
        )

        conn.commit()

    except sqlite3.IntegrityError:
        pass

    finally:
        conn.close()
        
def job_exists(url):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT 1 FROM jobs WHERE url = ?",
        (url,)
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None