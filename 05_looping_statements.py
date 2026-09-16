# 8/9/26


# in python, when we want to repeat a block of code, we use looping statements

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




#      11/9/26

n = int(input("enter a number:"))
lar = 0
for i in range(n):
    num = int(input("enter a number:"))
    if num > lar:
        lar=num
    print(lar)



n = int(input("enter a number:"))
count = 0

for i in range(2, n): # not including 1
    if n%i == 0:    # aka a number is divisible
        count = count + 1
        
if count == 0:
    print("it is a prime number")
else:
    print("non prime number")




for i in range(5):
    print(i, end="") # prints everything beside e/o due to end tag
    
for i in range(5):
    print("*", end="")
    
print("hi"*3)

print("*"*1)
print("*"*2)
print("*"*3)
print("*"*4)
print("*"*5)


n = int(input("enter:"))

for i in range(1, n+1):
    print("*"*i)
    

n = int(input("enter:"))

    
for i in range(1, n+1):
    print("#"*n)

12/9/26

n = int(input("enter a number: "))

for i in range(1, n+1):
    print(str(i)*i)
    
n = int(input("enter a number: "))

for i in range(1, n+1):
    print(str(i)*5)



n = int(input("enter:"))
num = 1

for i in range(1, n+1):
    for j in range(i):
       print(num, end="")
       num+=1
    print()
       
       
15/9/26

for i in range(1,4):
   print(i)
   for j in range(10,14):
      print(j)
      
