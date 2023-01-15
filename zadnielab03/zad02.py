import string
import random


def create_secure_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = random.choices(characters, k=random.randint(8, 18))
    password += random.choices(string.ascii_uppercase, k=2)
    password += random.choices(string.ascii_lowercase, k=2)
    password += random.choices(string.digits, k=1)
    password += random.choices(string.punctuation, k=1)
    random.shuffle(password)
    print("".join(password))


create_secure_password()
