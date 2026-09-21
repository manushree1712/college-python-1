# 17/9/26


# string methods

# 1) upper method - converts all lowercase letters to uppercase letters
#         name.upper()
        
name = "python"
print(name.upper())
print("python".upper())

name = input("enter name: ")
print(name.upper())

#   2) lower method - converts all uppercase letters to lowercase letters
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

name3 = "*******lalalalalalalalala*************"
print(name3.strip("*"))

#  7) L string - removes spaces only from the beginning of the string

stripL = "                        whteverr                          "
print(stripL.lstrip())

stripL2 = "$$$$$$$$$$$$$$$$$$dollllla bills$$$$$$$$$$$$$$$$$$$$$$$"
print(stripL2.lstrip("$"))

#  8) R string - removes spaces only from the ending of the string only


stripR = "                        whteverr                          "
print(stripR.rstrip())

stripR2 = "$$$$$$$$$$$$$$$$$$dollllla bills$$$$$$$$$$$$$$$$$$$$$$$"
print(stripR2.rstrip("$"))


#  9) replace method - replaces a piece of text with other
#               syntax:    name.replace(old,new)
#                                   - old word is old and is supposed to be replace by new

name = "i like icecream"

print(name)

print(name.replace("icecream","panipuri"))

#  19/9/26


#  10) split method - breaks a string and converts it into list. 
#                     by default, split method splits at spaces 


name = "python html c css javascript"
print(name.split())

fruits_1 = "apple-banana-orange-watermelon"
print(fruits_1.split("-"))


fruits = input("enter fruits: ")
print(fruits.split())
print(len(fruits.split()))

fruits_2 = "apple-banana-orange-watermelon-mango-strawberry-dragon fruit"
print(fruits_2.split("-",4))
# the 2 refers to only splittin upto 2 hypens


#  11) R split - it is similar to normal split but
# starts splitting from right side of the string

vegetable = "tomato-onion-bell peppers-corn-brinjal-potato"
print(vegetable.rsplit("-",3))

#  12) find - it is used to find the char position or index,
#             if the char is not there in the given string, it returns -1

finds = "i like python"
print(finds.find("python"))

finds = "i like python"
print(finds.find("java"))


finds = "apple apple mango"
print(finds.find("apple"))

#  13) R find - finds the last occurence unlike normal find

#  14) index - it is similar to normal find, 
#       it is used to find the index of the given character


ind = "banana"

print(ind.find("e"))
print(ind.index("e"))


#  when you want to find the position of the character,
# that is not present in the given string,
# - then find method returns -1 has the output
# - while index method states it has an error (value error)


# 21/9/26

# 15) count method - it is used to count the number 
# of characters repeated in a given string
#         syntax = name.count()

name = "banana"
print(name.count("a"))
print(name.count("n"))
print(name.count("f"))


text = input("enter a name: ")
print(text.count("o"))


# 16) startswith method - checks whether a string starts particular value,
#   it'll give output has boolean value (true/false)


word = "python programming language"
print(word.startswith("python"))


email = input("enter your email: ")
print(email.startswith("student"))


# 17) endswith method - checks whether a string ends with a particular value,
#    it'll give output has boolean value (true/false)

word = "python programming language"
print(word.endswith("language"))

email = input("enter your email: ")

# mail = (email.endswith("gmail.com"))

# print(mail)

# if mail == True:
#     print("valid email")
# else:
#     print("invalid email")

if email.endswith("gmail.com"):
    print("valid email")
else:
    print("invalid email")


# 18) isalpha method - checks whether all characters are alphabets
#    and the output is in boolean

fruit = "apple"
print(fruit.isalpha())


word = "hello world"
print(word.isalpha()) # space so false

# 19) isnumeric method - checks whether all characters are numbers
#    and the output is in boolean

num = "67895432"
print(num.isnumeric())

num2 = "is this numeric 23456789"
print(num2.isnumeric())

num3 = 67895432
print(num3.isnumeric()) # gives n error cuz these are ONLY string method

# 20) isalnum method - checks whether all characters are alphabets
#                     or numeric values

text = "al123b"
print(text.isalnum())


text2 = "al 1 2 3b"
print(text2.isalnum())


text3 = "water"
print(text3.isalnum())