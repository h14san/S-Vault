# S-Vault
## Personal Vault Security System (PVSS)

**S-Vault** is a command-line password managemer built in Python. It provides secure credential handling with **encryption, authentication, bcrypt hashing,** and persistent storage, designed so you never have to compromise security.  

## Features

- **Command-line interface** – lightweight and fast  
- **Encryption** – secure your stored credentials  
- **Authentication** – master-password protected access  
- **Bcrypt hashing** – safeguard sensitive data with industry-standard hashing  
- **Persistent storage** – uses `.json` and `.hash` files for reliability  

## Structure

- `svault.py` – main program logic  
- `resources.py` – helper functions and utilities (e.g., generate passwords, search credentials)  
- `.json` – stores user accounts securely  
- `.hash` – stores bcrypt-hashed sensitive data  

## Technologies & Libraries

- Python 3 and Libraries

## Usage

1. Clone the repository:  
```bash
git clone <repo-url>
```
2. Navigate to the project directory:
```bash
cd S-Vault
```
3. Run the vault and follow CLI prompts to add, remove, or search passwords.
```bash
python svault.py
```
