CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS saved_locations (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
