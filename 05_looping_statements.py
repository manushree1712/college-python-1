# 8/9/26


# in python, when we want to repeat a block of code, we use loopiing statements

# theres two types:
#   - for loop
#   - while loop


# for i in range(5):
#     print(i)   #counting starts from 0
    
# for i in range(101):
#     print(i)   #0-100
    
# for i in range(1,6):
#     print(i)   #inclusive so counts everything except 6
    
# for i in range(1,10,2):  
#     print(i)    #skips every second number + 10,  cuz inlusive
    
# for i in range(1,7,4):
#     print(i)
    
    
# for i in range(start,stop,step):

# n = int(input("give a number: "))

# for i in range(2,n+1,2):  #starts from 2 for even
#     print(i)
    
# for i in range(1,n+1,2):  #starts from 1 for odd
#     print(i)


n = int(input("enter a num: "))
print("even numbers are:")
for i in range(2,n+1, 2):
    print(i)
print("odd numbers are: ")
for i in range(1, n+1, 2):
    print(i)