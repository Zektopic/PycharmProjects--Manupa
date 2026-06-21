target = 600851475143
number = 1
larger_factors = []

while number <= int(target**0.5):
    if target % number == 0:
        num = number

        # To take input from the user
        # num = int(input("Enter a number: "))

        # prime numbers are greater than 1
        if num > 1:
            # check for factors
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    print(num, "is not a prime number")
                    break
            else:
                print(num, "is a prime number")

        # if input number is less than
        # or equal to 1, it is not prime
        else:
            print(num, "is not a prime number")

        larger_factor = target // number
        if larger_factor != number:
            larger_factors.append(larger_factor)

    number += 1

for num in reversed(larger_factors):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
