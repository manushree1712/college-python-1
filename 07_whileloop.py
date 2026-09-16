# 16/9/26

# while loop is used to repeat the block of code has long has condition is true

#       while loop:
#           #code


i = 1

while i <= 10:
    print(i)
    i += 1



i = 2

while i <= 10:
    if i%2 == 0:
     print(i)
    i += 2


i = 10

while i >= 1:
    print(i)
    i -= 1


n = int(input("enter a number: "))
total = 0
i = 1

while i <= n:
    if i%2 == 0:
        total += i
    i += 1
print(total) 

# ts pmo, i and n are correlated so instead of n,
# you work with i and take the addition wala shi has a diffrent variable