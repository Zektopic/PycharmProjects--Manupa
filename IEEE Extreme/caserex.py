import string

alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"

def decrypt():
    
    print("Welcome to Caesar Cipher Decryption.\n")
    encrypted_message = input("Enter the message you would like to decrypt: ").strip()
    print()
    key = int(input("Enter key to decrypt: "))
    
    decrypted_message = "".join([
        chr(((ord(c) - 97 - key) % 26) + 97) if 'a' <= c <= 'z' else c
        for c in encrypted_message
    ])

    print("\nDecrypting your message...\n")
    print("Stand by, almost finished...\n")
    print("Your decrypted message is:\n")
    print(decrypted_message)


if __name__ == '__main__':
    try:
        decrypt()
    except EOFError:
        pass