


def inp(a,b):
    c1 == True 
    c2 == False
    while(c1 == True):
        a = input("Enter first number: ")
        if(type(float(a)) == float):
            a = float(a)
            c1 = False
            c2 = True
        else:
            print("enter the vaule again")
            c1 = True
    while(c2 == True):
        b = input("Enter second number: ")
        if(type(float(b)) == float):
            b = float(b)
            c2 = False
        else:
            print("enter the vaule again")
            c2 = True    



def add(a,b):
    result = a+b
def substract(a,b):
    result = a-b
def multiply(a,b):
    result = a*b
def divide(a,b):
    result = a/b
def power(a,b):
    result = a**b
def reminder(a,b):
    result = a%b
def select_op(choice,a,b):
    if(choice == '#'):
        return -1
    elif(choice == '+'):
        inp(a,b)
        add()
        return 0
    elif(choice == '-'):
        substract(a,b)
    elif(choice == '*'):
        multiply(a,b)
    elif(choice == '/'):
        divide(a,b)
    elif(choice == '^'):
        power(a,b)
    elif(choice == '%'):
        reminder(a,b)



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
    a=0
    b=0
    select_op(choice,a,b)
    if(select_op(choice,a,b) == -1):
    #program ends here
        print("Done. Terminating")
        exit()
    else:        
        select_op(choice,a,b)       

  
