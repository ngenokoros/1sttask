maths=70
eng=80
phy=60
kis=44

total = maths + eng + phy + kis
average = total / 4

#
#
# if average >= 70:
#     grade = "A"
# elif average >= 60:
#     grade = "B"
# elif average >= 50:
#     grade = "C"
# elif average >= 40:
#     grade = "D"
# else:
#     grade = "A"
#
if average >=0 and average < 25:
 grade="D"
elif 25 <= average < 50:
    grade="C"
elif 50 <= average < 70:
    grade="B"
else:
    grade = "A"
print("The average :", average)
print("The grade :", grade)



# if maths >70 and eng >70:
#   print("success")
# else:
#     print("either of the subject equals less than 70")
# if maths ==70:
#     print("A")
# else:print("fail")
# if maths > 0:
#     print("the number is positive")
# elif maths < 0:
#     print("the number is negative")
# else:
#     print("the number is 0")