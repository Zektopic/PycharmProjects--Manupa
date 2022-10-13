# Program published on https://beginnersbook.com

# Python program to sum all the digits of an input number

num = int(input("Enter a Number: "))
result = 0
hold = num

# while loop to iterate through all the digits of input number
while num > 0:
    rem = num % 10
    result = result + rem
    num = int(num/10)

# displaying output
print("Sum of all digits of", hold, "is: ", result)