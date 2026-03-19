import secrets
import string
import json
import bcrypt
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
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
            print("Action not listed\n")
def save_password(app, password, key):
    f = Fernet(key)
    encrypted_pw = f.encrypt(password.encode()).decode()
    data = load_password()
    data[app] = encrypted_pw
    with open("passwords.json", "w") as f:
        json.dump(data, f)
def load_password():
    with open("passwords.json", "r") as f:
        return json.load(f)
def init_passwords():
    with open("passwords.json", "w") as f:
        json.dump({}, f)
def create_account(text):
    master_pw = bcrypt.hashpw(text.encode(), bcrypt.gensalt())
    with open("master.hash", "wb") as f:
        f.write(master_pw)
    init_passwords()
def login(text):
    with open("master.hash", "rb") as f:
        master_pw = f.read()
    if not master_pw:
        print("No account found. Please create one first\n")
        return None
    return bcrypt.checkpw(text.encode(), master_pw)
def after_login():
    while True:
        print("0. Exit")
        print("1. Enter A New Password")
        print("2. Generate Strong Password")
        print("3. View All Passwords")
        print("4. Search Passwords")
        n = get_number("Action: ")
        if n in range(0,5):
            return n
        else:
            print("Action not listed\n")
def derive_key(master_password):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"svault",
        iterations=100000,
    )
    key = kdf.derive(master_password.encode())
    return base64.urlsafe_b64encode(key)
def search_password(app, master_key):
    fernet = Fernet(master_key)
    data = load_password()
    if app in data:
        return fernet.decrypt(data[app].encode()).decode()
    else:
        return None