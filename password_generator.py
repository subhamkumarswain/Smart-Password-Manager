import random
import string

def generate_password(length: int) -> str:
    if length < 4:
        raise ValueError("Password length must be at least 4")

    # Ensure mandatory characters
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    symbol = random.choice(string.punctuation)

    # Remaining characters
    remaining_length = length - 4
    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining = ''.join(random.choice(all_chars) for _ in range(remaining_length))

    # Combine and shuffle
    password_list = list(upper + lower + digit + symbol + remaining)
    random.shuffle(password_list)

    return ''.join(password_list)
