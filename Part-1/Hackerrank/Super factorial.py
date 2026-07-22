
def part1(num):
    n = num
    total = 1
    count = n
    while count > 0 :
        count -= 1
        total *= n
        n -= 1
    return total


def main():
    try:
        num = int(input())
    except EOFError:
        return
    count_1 = num
    if 0 <= num <= 750 :
        total_1 = part1(num)
        while count_1 > 0 :
            total_1 *= num
            count_1 -= 1
        print(total_1)
    else:
        print("Invalid answer. ")

if __name__ == '__main__':
    main()
