import os
import sqlite3
import pickle

PASSWORD = "SuperSecret123!"

def login(user, password):
    if password == PASSWORD:
        print("Logged in")
    else:
        print("Wrong password")

def search_user(username):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    query = f"SELECT * FROM users WHERE name = '{username}'"
    cur.execute(query)
    return cur.fetchall()

def delete_file(name):
    os.system("rm " + name)

def insecure_pickle(path):
    return pickle.load(open(path, "rb"))

if __name__ == "__main__":
    login("admin", "SuperSecret123!")
    insecure_pickle("data.pkl")
