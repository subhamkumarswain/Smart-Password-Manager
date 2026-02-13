import json
import os
from encryption import encrypt_password, decrypt_password

FILE_NAME = "password_store.json"

def save_password(website: str, username: str, password: str):
    website = website.lower()

    data = {}

    # If file exists, load existing data
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}

    # Add new entry
    encrypted = encrypt_password(password)

    data[website] = {
    "username": username,
    "password": encrypted
    }


    # Save back to file
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

    print("Password saved successfully!")


def retrieve_password(website: str):
    website = website.lower()
    if not os.path.exists(FILE_NAME):
        print("No passwords stored yet.")
        return

    with open(FILE_NAME, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            print("No valid data found.")
            return

    if website in data:
        print("\nWebsite:", website)
        print("Username:", data[website]["username"])
        encrypted = data[website]["password"]
        decrypted = decrypt_password(encrypted)
        print("Password:", decrypted)

    else:
        print("No account found for this website.")


def update_password(website: str, new_password: str):
    if not os.path.exists(FILE_NAME):
        print("No passwords stored yet.")
        return

    with open(FILE_NAME, "r") as file:
        data = json.load(file)

    if website in data:
        encrypted = encrypt_password(new_password)
        data[website]["password"] = encrypted

        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

        print("Password updated successfully!")
    else:
        print("Website not found.")


def delete_password(website: str):
    if not os.path.exists(FILE_NAME):
        print("No passwords stored yet.")
        return

    with open(FILE_NAME, "r") as file:
        data = json.load(file)

    if website in data:
        del data[website]

        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

        print("Password deleted successfully!")
    else:
        print("Website not found.")
