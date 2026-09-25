# n = int(input("enter:"))

# for i in range(1, n+1):
#     print("*"*i)
    

# n = int(input("enter:"))

    
# for i in range(1, n+1):
#     print("#"*n)
    
    
# n = int(input())

# for i in range(1,n+1):
#     space = (n-i)*" "
#     star = i*"*"
#     print(space + star)
 

# space = (n-(i+1))
#  stars = 2i+1

n = int(input())

for i in range(0, n+1):
    space = (n-(i+1))*" "
    stars = (2*i+1)*"*"
    print(space + stars)