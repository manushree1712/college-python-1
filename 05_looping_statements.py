# 8/9/26


# in python, when we want to repeat a block of code, we use loopiing statements

# theres two types:
#   - for loop
#   - while loop


for i in range(5):
    print(i)   #counting starts from 0
    
for i in range(101):
    print(i)   #0-100
    
for i in range(1,6):
    print(i)   #inclusive so counts everything except 6
    
for i in range(1,10,2):  
    print(i)    #skips every second number + 10,  cuz inlusive
    
for i in range(1,7,4):
    print(i)
    
    
# for i in range(start,stop,step):

n = int(input("give a number: "))

for i in range(2,n+1,2):  #starts from 2 for even
    print(i)
    
for i in range(1,n+1,2):  #starts from 1 for odd
    print(i)


n = int(input("enter a num: "))
print("even numbers are:")
for i in range(2,n+1, 2):
    print(i)
print("odd numbers are: ")
for i in range(1, n+1, 2):
    print(i)
    
    
# 9/9/26
    
    

n = int(input("enter any num:"))
count = 0

for i in range(1, n+1):
    if i%2 == 0:
        count = count + 1
print(f" there are {count} even numbers")

count2 = 0

for i in range(1, n+1):
    if i%2 != 0:
        count2 = count2 + 1
print(f"there are {count2} odd numbers")


n = int(input("enter a numbers:"))
sum = 0

for i in range(1, n+1):
     sum = sum + i
print(sum)

n = int(input("enter a num:"))
sum = 0

for i in range(2,n+1,2):   # start with 2 to consider all even numbers
    sum = sum + i           # method 1
print(sum)

sum2 = 0

for i in range(1,n+1): 
    if   i%2 == 0:
        sum2 = sum2 + i           # method 2
print(sum2)


n = int(input("enter a num:"))
num = 1

for i in range(1,n+1):
    num = num*i
print(num)


# 10/9/26



n = int(input("enter a number: "))

for i in range(1,n+1):
    if i%5 == 0:
        print((i))
        
        
        

n = int(input("enter a number: "))
count = 0

for i in range(1,n+1):
    if i%5 == 0:
        count = count + 1        # count +=1
        # print((i))
print(f"there are {count} numbers divisible by 5")




name = (input("enter name:"))

for i in name:
    print(i)





n = (input("enter a number:"))
sum=0

for i in n:
    sum=sum+int(i)   #converting i-string into i-integer to add it one by one
print(sum)    



n = int(input("enter how many numbers do you want:"))


for i in range(1,n+1):

    num=int(input(f"give a number:"))
    
    print(num)


