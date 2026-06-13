import unittest
import importlib
import hashlib
import os

TEST_HASH = "d48c4268e1cfaa8ddb4a1643d07d6638:18fe6b1d28b7727f534db9b9158dce9238c7a5e52093ee1cdf7c902f9ffb4258"
os.environ["APP_PASSWORD_HASH"] = TEST_HASH

# Import the module with a hyphen in the name
test_1 = importlib.import_module("Part-1.wHATTA.Basics.Test-1")
check_password = test_1.check_password
hash_password = test_1.hash_password

class TestCheckPassword(unittest.TestCase):
    def test_correct_password(self):
        self.assertTrue(check_password("9", TEST_HASH))

    def test_incorrect_password(self):
        self.assertFalse(check_password("wrongpassword", TEST_HASH))

    def test_empty_password(self):
        self.assertFalse(check_password("", TEST_HASH))

    def test_different_valid_hash(self):
        password = "newpassword123"
        expected_hash = hash_password(password)
        self.assertTrue(check_password(password, expected_hash))

    def test_special_characters(self):
        password = "!@#$%^&*()_+"
        expected_hash = hash_password(password)
        self.assertTrue(check_password(password, expected_hash))

if __name__ == '__main__':
    unittest.main()
