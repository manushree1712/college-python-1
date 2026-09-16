#  15/9/26

# in python, break statement is used to immediatly stop a loop.

for i in range(1,10):
    if i == 5:
        break
    print(i)
    
    
lst = [1,3,2,4,5]

for i in lst:
    print(i)
    
list = ['vaishu', 'anu', 'hima', 'pari', 'pallabiii']

for i in list:
    print(i)
    
    
lst = [1,3,2,4,5]

for i in lst:
    if i%2 == 0:
        print(i)
        break
    
    
# continue statement is used to skip the particular value

for i in range(1,11):
    if i ==7:
        continue
    print(i)

for i in range(1,21):
    if i%5 == 0:
        continue
    print(i)


# 16/9/26


for i in ResourceWarning(1,11):
    if i == 3:
        continue
    if i == 7:
        break