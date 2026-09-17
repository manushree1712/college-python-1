# # string is a set of characters written in double quote

# # every character inside a string has its own index
# #indexs start from zero


# # [-6,-5,-4,-3,-2,-1]
# # [p,y,t,h,o,n]
# # [0,1,2,3,4,5]


name = "hello world"

print(name[0:5])  # direct upto 4
print(name[6:])   # starts from 6
print(name[:])    # gives full word
print(name[0:8:2]) # 0 to 7 and skips odd
print(name[::2])  # gives full but skips odd index
print(name[::-1]) # reverses the word


# ---------------------------------------------------------------------------

# slicing in python is taking a small part from string
# name[start:end]  --- end is inclusive

name = 'python'
print(name[0:5])



# 17/9/26

# we use length function to find the length of the given string


name = "python"
print(len(name))

name = str(input("enter name: "))
print(len(name))



