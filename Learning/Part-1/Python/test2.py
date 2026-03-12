


def inp():
    c1 = True
    c2 = False
    a = 0.0
    b = 0.0
    while(c1 == True):
        a = input("Enter first number: ")
        try:
            a = float(a)
            c1 = False
            c2 = True
        except ValueError:
            print("enter the vaule again")
            c1 = True
    while(c2 == True):
        b = input("Enter second number: ")
        try:
            b = float(b)
            c2 = False
        except ValueError:
            print("enter the vaule again")
            c2 = True
    return a, b



def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def power(a,b):
    return a**b
def reminder(a,b):
    return a%b
def select_op(choice):
    if(choice == '#'):
        return -1
    elif(choice == '$'):
        return 0
    elif(choice in ('+', '-', '*', '/', '^', '%')):
        a, b = inp()
        if(choice == '+'):
            print(f"{a} + {b} = {add(a, b)}")
        elif(choice == '-'):
            print(f"{a} - {b} = {substract(a, b)}")
        elif(choice == '*'):
            print(f"{a} * {b} = {multiply(a, b)}")
        elif(choice == '/'):
            if b == 0:
                print("float division by zero")
                print(f"{a} / {b} = None")
            else:
                print(f"{a} / {b} = {divide(a, b)}")
        elif(choice == '^'):
            print(f"{a} ^ {b} = {power(a, b)}")
        elif(choice == '%'):
            print(f"{a} % {b} = {reminder(a, b)}")
    else:
        print("Unrecognized operation")



while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
  
    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    if(select_op(choice) == -1):
        #program ends here
        print("Done. Terminating")
        exit()

  
