num1 = input("Enter you first number: ")
num2 = input("Enter you second number: ")
choice = input("Do you want to add(a) / substract(s) / mmultiply(m) / divide(d) ? ")
if choice == 'a' :
    add = int(num1)+int(num2)
    print("The addition is " + str(add))
elif choice == 's' :
    subs = int(num1)-int(num2)
    print("The substraction is " + str(subs))
elif choice == 'm' :
    mult = int(num1)*int(num2)
    print("The multipication is " + str(mult))
elif choice == 'd' :
    if int(num2) == 0:
        print("Cannot divide by zero")
    else:
        div = int(num1)/int(num2)
        print("The division is " + str(div))

try:
    input(""".............Thank you.............
Please press the ENTER button""")
except EOFError:
    pass