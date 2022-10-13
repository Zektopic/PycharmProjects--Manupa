
def part1():
    n = ass
    total = 1
    total_1 = total
    count = n
    while count > 0 :
        count -= 1
        total *= n
        n -= 1
        total_1 = total


ass = int(input())
count_1 = ass
if 0 <= ass <= 750 :
    while count_1 > 0 :
        part1()
        total_1 *= ass
        count_1 -= 1
    print(total_1)
else:
    print("Invalid answer. ")
