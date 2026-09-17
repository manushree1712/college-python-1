# 17/9/26


# string methods

# 1) upper method - converts all lowercase letters to uppercase letters
#         name.upper()
        
name = "python"
print(name.upper())
print("python".upper())

name = input("enter name: ")
print(name.upper())

# #  2) lower method - converts all uppercase letters to lowercase letters
#         #  name.lower()
        
low = "FoOd"
print(low.lower())

#  3) capitalize method - converts only first character into 
#       uppercase rest are left as lowercase
#          name.capitalize()
        
cap = "i love python"
print(cap.capitalize())

cap2 = "i Love Python"
print(cap2.capitalize())

cap3 = "i love python. i love food"
print(cap3.capitalize())

cap4 = input("enterrrrr: ")
print(cap4.capitalize())

#  4) title method - converts first letter of eacch word into uppsercase
#         name.title()
        
title1 = "i love food"
print(title1.title())

title2 = "i Love Python"
print(title2.title())

title3 = "i love python. i love food"
print(title3.title())

title4 = input("enterrrrr: ")
print(title4.title())


#  5) swapcase method - converts lower to upppercase and vice versa
#          name.swapcase()
        
name = "FOOOD i want"
print(name.swapcase())

swap = input("enters:")

print(swap.swapcase())


#  6) strip method - it is used to remove the wide spaces from the
# begininng to the ending of the string, it wont remove the spaces
# in between the string
#         name.strip()

name ="                  this is      python                    "

print(name)
print(name.strip())

name2 = input("enterrrrr:")

print(name2)
print(name2.strip())