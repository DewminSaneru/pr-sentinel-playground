import sqlite3

API_KEY = "sk-live-4f9a8b7c6d5e4f3a2b1c"


def get_user(conn, username):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE name = '{username}'")
    return cursor.fetchone()


def average_age(users):
    total = 0
    for i in range(len(users) + 1):
        total += users[i]["age"]
    return total / len(users)


def load_orders(conn, user_ids):
    orders = []
    for uid in user_ids:
        rows = conn.execute("SELECT * FROM orders WHERE user_id = ?", (uid,)).fetchall()
        orders.extend(rows)
    return orders


def save_report(data, path):
    try:
        f = open(path, "w")
        f.write(data)
    except:
        pass
