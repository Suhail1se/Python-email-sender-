import hashlib
import json
import os

DB_FILE = 'users.json'

def load_users():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, 'r') as file:
        return json.load(file)

def save_users(users):
    with open(DB_FILE, 'w') as file:
        json.dump(users, file)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    users = load_users()
    if username in users:
        print("Username already exists.")
        return
    users[username] = hash_password(password)
    save_users(users)
    print("User registered successfully.")

def login(username, password):
    users = load_users()
    if username not in users:
        print("Username does not exist.")
        return
    if users[username] == hash_password(password):
        print("Login successful!")
    else:
        print("Invalid password.")

while True:
    action = input("Choose action (register/login/exit): ").strip().lower()
    if action == "exit":
        break
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    if action == "register":
        register(username, password)
    elif action == "login":
        login(username, password)
    else:
        print("Invalid action.")
