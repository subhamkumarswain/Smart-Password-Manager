import hashlib
import os

MASTER_FILE = "master.hash"

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def set_master_password(password: str):
    hashed = hash_password(password)

    with open(MASTER_FILE, "w") as file:
        file.write(hashed)

def verify_master_password(password: str) -> bool:
    if not os.path.exists(MASTER_FILE):
        return False

    hashed = hash_password(password)

    with open(MASTER_FILE, "r") as file:
        stored_hash = file.read()

    return hashed == stored_hash

