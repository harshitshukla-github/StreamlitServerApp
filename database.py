import sqlite3


def create_connection():
    conn = sqlite3.connect('user_data.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (username, password) 
        VALUES (?, ?)
    ''', (username, password))
    conn.commit()
    conn.close()

def verify_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE username = ? AND password = ?
    ''', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user