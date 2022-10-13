

def breaker():
    return 0
def add(a,b):
    result = a+b
    print( str(a) +  " + " +str(b )+ " = "+ str(result) )
def substract(a,b):
    result = a-b
    print( str(a) +  " - " +str(b )+ " = "+ str(result) )
def multiply(a,b):
    result = a*b
    print( str(a) + " * " +str(b )+ " = "+ str(result) )
def divide(a,b):
    if(b != 0):
        result = a/b
        print( str(a) + " / " +str(b )+" = "+ str(result) )
    else: 
        print("float division by zero")
        print( str(a) + " / " +str(b )+" = "+ "None" )
def power(a,b):
    result = a**b
    print( str(a) + " ^ " +str(b )+ " = "+ str(result) )
def reminder(a,b):
    result = a%b
    print( str(a) + " % " +str(b )+ " = "+ str(result) )
def select_op(choice):
    if(choice == '#'):
        return -1
    elif(choice == '$'):
        return 1
    if(choice == '+'):
        return 0
    elif(choice == '-'):
        return 0
    elif(choice == '*'):
        return 0
    elif(choice == '/'):
        return 0
    elif(choice == '^'):
        return 0
    elif(choice == '%'):
        return 0
    else:
         print("Unrecognized operation")

        
def other(choice,a,b):        
    if(choice == '+'):
        add(a,b)
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
    elif(choice == '#'):
        return -1
    elif(choice == '$'):
        return 1



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
    print(choice)
    select_op(choice)
    if(select_op(choice) == -1):
    #program ends here
        print("Done. Terminating")
        exit()
    elif(select_op(choice) == 0):        
        c1 = True 
        c2 = False
        while(c1 == True):
            a = input("Enter first number: ")
            print(a)
            try:
                a = float(a)
                c1 = False
                c2 = True
            except:
                if(a[-1]=='$'):
                    choice = '$'
                    select_op(choice)
                    b ="1"
                    break
                elif(a[-1]=='#'):
                    print("Done. Terminating")
                    exit()
                else:
                    print("Not a valid number,please enter again")
                    c1 = True
        while(c2 == True):
            b = input("Enter second number: ")
            print(b)
            try:
                b = float(b)
                c2 = False
            except:
                if(b[-1]=="$"):
                    choice = '$'
                    select_op(choice)
                    b ="1"
                    break
                elif(b[-1]=='#'):
                    print("Done. Terminating")
                    exit()
                else:
                    print("Not a valid number,please enter again")
                    c2 = True
        other(choice,a,b)
    elif(select_op(choice) == 1):
        True

