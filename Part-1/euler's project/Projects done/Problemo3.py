divisor = 0
for item in range(1, 600851475143 , 2):
    divisor = item
    if 600851475143 % divisor == 0 :
       print(divisor)
       print("ALlla " + str(600851475143 // divisor))


