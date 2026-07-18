import string

alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"

def decrypt():
    
    print("Welcome to Caesar Cipher Decryption.\n")
    encrypted_message = input("Enter the message you would like to decrypt: ").strip()
    print()
    key = int(input("Enter key to decrypt: "))
    
    decrypted_message = []

    for c in encrypted_message:

        if 'a' <= c <= 'z':
            position = ord(c) - 97
            new_position = (position - key) % 26
            new_character = chr(new_position + 97)
            decrypted_message.append(new_character)
        else:
            decrypted_message.append(c)

    decrypted_message = "".join(decrypted_message)

    print("\nDecrypting your message...\n")
    print("Stand by, almost finished...\n")
    print("Your decrypted message is:\n")
    print(decrypted_message)

decrypt()