number = 1
target = 8462696833
large_factors = []
while number * number <= target:
    if target % number == 0:
        print(number)
        if number * number != target and number != 1:
            large_factors.append(target // number)
    number += 1

for factor in reversed(large_factors):
    print(factor)

input("  ")