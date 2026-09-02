# Given three ints, a b c, return True if one of b or c is "close" 
# (differing from a by at most 1), while the other is "far",
# differing from both other values by 2 or more. Note: abs(num) computes the 
# absolute value of a number.


# close_far(1, 2, 10) → True
# close_far(1, 2, 3) → False
# close_far(4, 1, 3) → True

# abs = absolute

a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))

print((a,b,c))

if abs(a-b) <= 1:
    if abs(b-c)>=2 and abs(a-c)>=2:
        print("true")
    else:
        print("false")
elif abs(a-c) <=1:
    if abs(a-b) >= 2 and abs(b-c) >= 2:
        print("true")
    else:
        print("false")
else: 
    print("false")