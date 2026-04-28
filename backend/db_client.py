import sqlite3

class DBClient:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row

    def init_db(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                goal TEXT NOT NULL
            )
        ''')
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS workouts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                type TEXT NOT NULL,
                duration INTEGER NOT NULL,
                calories INTEGER NOT NULL
            )
        ''')
        self.conn.commit()

    def save_profile(self, data: dict) -> int:
        cursor = self.conn.execute(
            "INSERT INTO users (name, goal) VALUES (?, ?)",
            (data["name"], data["goal"])
        )
        self.conn.commit()
        return cursor.lastrowid

    def get_profile(self, user_id: int) -> dict:
        cursor = self.conn.execute(
            "SELECT name, goal FROM users WHERE id = ?",
            (user_id,)
        )
        row = cursor.fetchone()
        if row:
            return dict(row)
        return {}

    def log_workout(self, data: dict) -> int:
        cursor = self.conn.execute(
            "INSERT INTO workouts (user_id, type, duration, calories) VALUES (?, ?, ?, ?)",
            (data["user_id"], data["type"], data["duration"], data["calories"])
        )
        self.conn.commit()
        return cursor.lastrowid

    def get_workout(self, log_id: int) -> dict:
        cursor = self.conn.execute(
            "SELECT user_id, type, duration, calories FROM workouts WHERE id = ?",
            (log_id,)
        )
        row = cursor.fetchone()
        if row:
            return dict(row)
        return {}

    def get_user_workouts(self, user_id: int) -> list[dict]:
        cursor = self.conn.execute(
            "SELECT id, user_id, type, duration, calories FROM workouts WHERE user_id = ?",
            (user_id,)
        )
        return [dict(row) for row in cursor.fetchall()]
