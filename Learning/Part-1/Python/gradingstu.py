total = 0
n = input()
grade = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(1, int(n) + 1):
    grade[i] = input()
    if int(grade[i]) <= 100 and int(grade[i]) >= 0:
        if int(grade[i]) >= 40:
            if int(grade[i])% 10 >=3:
                grade[i] = int(grade[i]) + (5 - int(grade[i])% 10)
                total = total + grade[i]
            else:
                total = total + int(grade[i])
        else:
            total = total + int(grade[i])
    else:
        print("-1")
        
print(total/int(n) +1)