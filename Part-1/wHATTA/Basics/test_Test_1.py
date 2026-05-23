import unittest
import importlib
import hashlib
import os

TEST_HASH = "19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7"
os.environ["APP_PASSWORD_HASH"] = TEST_HASH

# Import the module with a hyphen in the name
test_1 = importlib.import_module("Part-1.wHATTA.Basics.Test-1")
check_password = test_1.check_password

class TestCheckPassword(unittest.TestCase):
    def test_correct_password(self):
        self.assertTrue(check_password("9", TEST_HASH))

    def test_incorrect_password(self):
        self.assertFalse(check_password("wrongpassword", TEST_HASH))

    def test_empty_password(self):
        self.assertFalse(check_password("", TEST_HASH))

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
