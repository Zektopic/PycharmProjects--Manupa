def main():
    i = 1
    while i == 1:
        try:
            answer = input(">")
        except EOFError:
            break

        if answer.lower() == "start":
            print("The car is started moving..")
        elif answer.lower() == "stop":
            print("The car stopped moving.")
        elif answer.lower() == "help":
            print("""start - start the car
    stop = to stop the car
    quit - to exit""")
        elif answer.lower() == "quit":
            print(" App closing ..... Press ENTER")
            i = i + 1
        else:
            print("I don't understand? ")


if __name__ == '__main__':
    main()
