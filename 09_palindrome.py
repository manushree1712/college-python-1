#  19/9/26

num = int(input("enter a num: "))

num1 = str(num)
num2 = num1[::-1]

if num == int(num2):
    print("it is a palindrome")
else:
    print("it is not a palindrome")
    