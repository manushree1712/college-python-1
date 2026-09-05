# 1/9/26

# Given 2 ints, a and b, return their sum. However,
# sums in the range 10..19 inclusive, are forbidden,
# so in that case just return 20.

# sorta_sum(3, 4) → 7
# sorta_sum(9, 4) → 20
# sorta_sum(10, 11) → 21


a = int(input("enter a number: "))
b = int(input("enter a number: "))

sum = a+b

if 10<=sum<=19:
    print(20)
    
else:
    print(f"({a},{b}) is {sum}")
    
    