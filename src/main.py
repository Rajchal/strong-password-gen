import random
import string

def generate_password(length=16):
    if length < 4:  # Ensure minimum length to include all character types
        raise ValueError("Password length should be at least 4")

    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_letters),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]
    password += random.choices(all_characters, k=length - 3)
    random.shuffle(password)
    return ''.join(password)

def main():
    length = int(input("Enter the desired password length: "))
    print(generate_password(length))

if __name__ == "__main__":
    main()