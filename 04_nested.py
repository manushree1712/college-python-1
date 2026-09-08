# 7/9/26

#  nested if is when condition #2 depends on condition #1,,
#       if condition 1 executes well then only it'll move to condition 2

num = int(input("enter a num:"))


if num > 0:
    if num%2 == 0:
        print("even")
    else:
        print("odd")
else:
    print("not a positive number")
    
    
# 8/9/26
#  example 2


age = int(input("enter age: "))

if age >= 18:
    # liscence = int(input("yes(1) or no(0):"))
    liscence = (input("yes or no:"))
    if liscence == "yes":  
         print("you can drive!")
    # if liscence == "no":
    #      print("get a liscence to drive!")
    else:
        print("get a liscence to drive!")
else:
    print("you are NOT eligible to drive")



# example 3

attendence = int(input("enter attendence %: "))


if attendence >= 75:
    marks = int(input("enter marks: "))
    if marks >= 40:
        print("ELIGIBLE FOR A SCHLOARSHIP")
    else:
        print("NOT ELIGIBLE")
else:
    print("attendence shortage")