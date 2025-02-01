# src/password_generator.py

import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the password length: "))
    print("Generated password:", generate_password(length))

if __name__ == "__main__":
    main()
