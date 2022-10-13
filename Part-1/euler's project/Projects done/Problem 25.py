i_1 = "0"
i_2 = "1"
total = 0
count = 1
Rand_total = 0
while len(str(Rand_total)) < 1000 :
    count += 1
    total = int(i_1) + int(i_2)
    i_1 = int(i_2)
    i_2 = total
    if total % 2 == 0 :
        Rand_total += total
print(count)
