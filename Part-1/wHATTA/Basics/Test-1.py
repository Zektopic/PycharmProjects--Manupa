attempt = input("Enter the password: ")
i = 1
while i < 4 :
    i = i + 1
    if attempt == '9' :
        print("Congratulations!. You have entered the correct password. ")
        break
    elif i < 4:
        attempt = input("""Sorry wrong password. Reenter password: """)
else :
    print("Locked out.")
