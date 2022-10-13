i_1 = input("Zero; ")
i_2 = input("One: ")
total = 0
limit = input("final number: ")
Rand_total = 0
while total < int(limit) :
    print(total)
    total = int(i_1) + int(i_2)
    i_1 = int(i_2)
    i_2 = total
    if total % 2 == 0 :
        Rand_total += total
print("Answer {}".format(Rand_total))

