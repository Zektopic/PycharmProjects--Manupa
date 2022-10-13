start = input("Starting number: ")
stop = input("Stopping number: ")
total = 0
if int(start) % 3 == 0 :
    for item in range(int(start) , int(stop) + 1 , 3):
        total += item
    print("the Total is: {}".format(total))
else :
    start = int(start) + 1
    if int(start) % 3 == 0:
        for item in range(int(start), int(stop) + 1, 3):
            total += item
        print("the Total is: {}".format(total))

    else :
        start = int(start) + 1
        if int(start) % 3 == 0:
            for item in range(int(start), int(stop) + 1, 3):
                total += item
            print("the Total is: {}".format(total))
