total = 1
n = int(input())
count = n
if 0 <= n <= 750 :
    while count > 0 :
        count -= 1
        total *= n
        n -= 1
    print(total)
else:
    print("Invalid answer. ")