marks = float(input("Enter the marks obtained: "))
if marks < 60 :
    remark = "Weak"
elif 70 > marks >= 60 :
    remark = "Average"
elif 80 > marks >= 70 :
    remark = "Good"
elif 90 > marks >= 80 :
    remark = "Very Good"
elif 100 > marks >= 90 :
    remark = "Excellent"
else:
    remark = "Superb"
print(remark)