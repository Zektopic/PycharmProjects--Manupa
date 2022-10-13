# Python Program to print Prime Numbers from 1 to N

minimum = int(input(" Please Enter the Minimum Value: "))
maximum = int(input(" Please Enter the Maximum Value: "))
total = 0

Number = minimum

while (Number <= maximum):
    count = 0
    i = 2

    while (i <= Number // 2):
        if (Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        print(" %d" % Number, end='  ')
        total = total + Number
    Number = Number + 1

print("\n\nSum of Prime Numbers from %d to %d = %d" % (minimum, maximum, total))