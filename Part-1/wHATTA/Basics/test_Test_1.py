import unittest
import importlib
import hashlib

# Import the module with a hyphen in the name
test_1 = importlib.import_module("Part-1.wHATTA.Basics.Test-1")
check_password = test_1.check_password
DEFAULT_HASH = test_1.DEFAULT_HASH

class TestCheckPassword(unittest.TestCase):
    def test_correct_password(self):
        self.assertTrue(check_password("9", DEFAULT_HASH))

    def test_incorrect_password(self):
        self.assertFalse(check_password("wrongpassword", DEFAULT_HASH))

    def test_empty_password(self):
        self.assertFalse(check_password("", DEFAULT_HASH))

    def test_different_valid_hash(self):
        password = "newpassword123"
        expected_hash = hashlib.sha256(password.encode()).hexdigest()
        self.assertTrue(check_password(password, expected_hash))

    def test_special_characters(self):
        password = "!@#$%^&*()_+"
        expected_hash = hashlib.sha256(password.encode()).hexdigest()
        self.assertTrue(check_password(password, expected_hash))

if __name__ == '__main__':
    unittest.main()
