from .database import get_connection

def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def register_user(username, password, email):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, password, email))
    conn.commit()
    conn.close()
