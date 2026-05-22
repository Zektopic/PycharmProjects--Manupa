import hashlib
import os
import getpass
import sys

def check_password(entered_password, stored_hash):
    return hashlib.sha256(entered_password.encode()).hexdigest() == stored_hash

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
