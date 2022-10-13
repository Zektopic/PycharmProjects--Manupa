i = 1
answer = input(">")
while i == 1:
    if answer.lower() == "start":
        print("The car is started moving..")
        answer = input(">")
    elif answer.lower() == "stop":
        print("The car stopped moving.")
        answer = input(">")
    elif answer.lower() == "help":
        print("""start - start the car
    stop = to stop the car
    quit - to exit""")
        answer = input(">")
    elif answer.lower()  == "quit":
        print(" App closing ..... Press ENTER")
        i = i + 1
    else:
        print("I don't understand? ")
        answer = input(">")