# #1/9/26

# You are driving a little too fast, and a police officer stops you.
# Write code to compute the result, encoded as an int value: 0=no ticket,
# 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0.
# If speed is between 61 and 80 inclusive, the result is 1.
# If speed is 81 or more, the result is 2. Unless it is your birthday -- 
# on that day, your speed can be 5 higher in all cases.


# caught_speeding(60, False) → 0
# caught_speeding(65, False) → 1
# caught_speeding(65, True) → 0


speed = int(input("enter speed:"))
print(speed)
is_birthday = int(input("enter 0 or 1: "))
print(is_birthday)

if is_birthday:
    if speed<=65:
        print("no ticket")
    elif 66<=speed<=85:
        print("one small ticket")
    else:
        print("one big ticket")
        
else:
    if speed<=60:
            print("no ticket")
    elif 61<=speed<=80:
            print("one small ticket")
    else:
            print("one big ticket")
            

        
        
