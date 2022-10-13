number = 1
while number < 600851475143 :
    if 600851475143 % number == 0:
        num = number

        # To take input from the user
        # num = int(input("Enter a number: "))

        # prime numbers are greater than 1
        if num > 1:
            # check for factors
            for i in range(2, num):
                if (num % i) == 0:
                    print(num, "is not a prime number")

                    break
            else:
                print(num, "is a prime number")

        # if input number is less than
        # or equal to 1, it is not prime
        else:
            print(num, "is not a prime number")
        number += 1
    else:
        number += 1
