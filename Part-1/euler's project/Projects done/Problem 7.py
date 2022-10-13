Number = 1
turn = 1
while turn < 10002 :
    count = 0
    i = 2

    while (i <= Number // 2):
        if (Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        print(" %d" % Number, end='  ')
        turn += 1
        print("the turn is  " + str(turn))
    Number = Number + 1
