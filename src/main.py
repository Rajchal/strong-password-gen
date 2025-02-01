import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    # Define character sets
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    digit_chars = string.digits
    special_chars = string.punctuation

    # Combine character sets based on user preferences
    all_chars = ""
    if use_uppercase:
        all_chars += uppercase_chars
    if use_lowercase:
        all_chars += lowercase_chars
    if use_digits:
        all_chars += digit_chars
    if use_special:
        all_chars += special_chars

    # Ensure at least one character set is selected
    if not all_chars:
        raise ValueError("At least one character set must be selected")

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Example usage
password_length = 16  # Customize the password length
password = generate_password(length=password_length)
print(f"Generated Password: {password}")
