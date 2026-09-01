# 1/9/26

# Given 3 int values, a b c, return their sum.
# However, if one of the values is the same as another of the values,
# it does not count towards the sum.


# lone_sum(1, 2, 3) → 6
# lone_sum(3, 2, 3) → 2
# lone_sum(3, 3, 3) → 0

a = int(input("enter a number: "))
b = int(input("enter a number: "))
c = int(input("enter a number: "))


if a==b==c:
    print(0)
elif a==b:
    print(c)
elif b==c:
    print(a)
elif a==c:
    print(b)
else: 
    print(a+b+c)