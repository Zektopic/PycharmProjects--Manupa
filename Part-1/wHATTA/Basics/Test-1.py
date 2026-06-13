import hashlib
import os
import getpass
import sys
import secrets
import binascii

def hash_password(password):
    salt = secrets.token_hex(16)
    pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
    return f"{salt}:{binascii.hexlify(pwd_hash).decode('ascii')}"

def check_password(entered_password, stored_hash):
    try:
        salt, hash_hex = stored_hash.split(':', 1)
        pwd_hash = hashlib.pbkdf2_hmac('sha256', entered_password.encode('utf-8'), salt.encode('utf-8'), 100000)
        return secrets.compare_digest(binascii.hexlify(pwd_hash).decode('ascii'), hash_hex)
    except ValueError:
        return False

stored_password_hash = os.environ.get("APP_PASSWORD_HASH")
if not stored_password_hash:
    raise RuntimeError("APP_PASSWORD_HASH environment variable is not set")

def secure_input(prompt):
    if sys.stdin.isatty():
        return getpass.getpass(prompt)
    else:
        print(prompt, end='', flush=True)
        return sys.stdin.readline().rstrip('\n')

if __name__ == "__main__":
    attempt = secure_input("Enter the password: ")
    i = 1
    while i < 4 :
        i = i + 1
        if check_password(attempt, stored_password_hash):
            print("Congratulations!. You have entered the correct password. ")
            break
        elif i < 4:
            attempt = secure_input("Sorry wrong password. Reenter password: ")
    else :
        print("Locked out.")
