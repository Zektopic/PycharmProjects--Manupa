num1 = input("Enter you first number: ")
num2 = input("Enter you second number: ")
choice = input("Do you want to add(a) / substract(s) / mmultiply(m) / divide(d) ? ")
add = int(num1)+int(num2)
subs = int(num1)-int(num2)
mult = int(num1)*int(num2)
div = int(num1)/int(num2)
if choice == 'a' :
    print("The addition is " + str(add))
elif choice == 's' :
    print("The substraction is " + str(subs))
elif choice == 'm' :
    print("The multipication is " + str(mult))
elif choice == 'd' :
    print("The division is " + str(div))
input(""".............Thank you............. 
Please press the ENTER button""")