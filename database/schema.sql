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
);