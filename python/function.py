def myfunc():
    return 6+8
print(myfunc())
#
# def kk():
# #     print("hello kim")
# #
# # kk()
# #
# # # n=50
# def square(n):
#      return n*n+9
# # return n ** 2 #another way for square
# print(square(50))
#
#
# def squared(n):
#     return n*n*n
# print(squared(60))
#
from functools import total_ordering
#
# def name(kim):
#     return ("my name is " + kim)
# #
# print(name("kim"))
# #
# math= input("Enter a math: ")
# english= input("Enter a english : ")
#
# total=math+english
# print("the sum is"+total)

num = int(input("number: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

