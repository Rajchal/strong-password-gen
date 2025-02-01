# tests/test_password_generator.py

import unittest
from src.password_generator import generate_password
import string

class TestPasswordGenerator(unittest.TestCase):
    def test_password_length(self):
        length = 16
        password = generate_password(length)
        self.assertEqual(len(password), length)

    def test_password_content(self):
        password = generate_password()
        has_letter = any(char.isalpha() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_punctuation = any(char in string.punctuation for char in password)
        self.assertTrue(has_letter)
        self.assertTrue(has_digit)
        self.assertTrue(has_punctuation)

if __name__ == '__main__':
    unittest.main()
