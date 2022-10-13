i = 1
range_1 = 100
total = 0
while range_1 > 0 :
    total += i**2
    i += 1
    range_1 -= 1
number_1 = sum(range(1,101))
print(number_1)
total_1 = number_1**2
final = total_1 - total
print(final)