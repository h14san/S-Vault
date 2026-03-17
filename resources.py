import secrets
import string
import json
import bcrypt
def get_number(input_text):
    while True:
        try:
            num = int(input(input_text))
            return num
        except ValueError:
            print("Invalid Input. Please Try Again")
def generate_password(n):
    SPECIAL = "!@#$%^&*()-_=+[]{}|;:,.<>?"
    characters = string.ascii_letters + string.digits + SPECIAL
    required = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(SPECIAL),
    ]
    rest = [secrets.choice(characters) for i in range(n - len(required))]
    pool = required + rest
    secrets.SystemRandom().shuffle(pool)
    return "".join(pool)
def authenticate():
    while True:
        print("0. Exit")
        print("1. Login")
        print("2. Create Account")
        n = get_number("Action: ")
        if n in range(0,3):
            return n
        else:
            print("Action not listed")
def save_password(text):
    with open("passwords.json", "w") as f:
        json.dump(text,f)
def load_password():
    with open("passwords.json","r") as f:
        text = json.load(f)
def create_account(text):
    master_pw = bcrypt.hashpw(text.encode(), bcrypt.gensalt())
    with open("master.hash", "wb") as f:
        f.write(master_pw)
def login(text):
    with open("master.hash", "rb") as f:
        master_pw = f.read()
    return bcrypt.checkpw(text.encode(), master_pw)
