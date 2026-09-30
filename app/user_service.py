import sqlite3


def get_user(conn, username):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ?", (username,))
    return cursor.fetchone()


def average_age(users):
    if not users:
        return 0
    return sum(u["age"] for u in users) / len(users)
