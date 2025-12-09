import sqlite3

def search_user(user_input):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    query = f"SELECT * FROM users WHERE name = '{user_input}'"  # SQL Injection
    print("Executing query:", query)
    cur.execute(query)

    return cur.fetchall()

def run_eval(code):
    eval(code)  # extremely unsafe

def render_html(name):
    return f"<html><body>Hello {name}</body></html>"  # XSS

if __name__ == "__main__":
    name = input("Enter username: ")
    print(search_user(name))

    evil = input("Enter code to eval: ")
    run_eval(evil)  # 100% critical
