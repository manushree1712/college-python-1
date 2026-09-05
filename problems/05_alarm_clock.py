# 2/9/26
 
 
# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, 
# and a boolean indicating if we are on vacation, return a string of the form
# "7:00" indicating when the alarm clock should ring. Weekdays, 
# the alarm should be "7:00" and on the weekend it should be "10:00".
# Unless we are on vacation -- then on weekdays it should be "10:00" and 
# weekends it should be "off".


# alarm_clock(1, False) → '7:00'
# alarm_clock(5, False) → '7:00'
# alarm_clock(0, False) → '10:00'



day = int(input("enter a day:"))
is_vacation = int(input("enter 0 or 1:"))

if is_vacation: #if 1
    if 1<=day<=5:
        print(f"({is_vacation},{day}) is 10:00 AM")
    else:
        print("OFF")
        
else: # if 0
    if 1<=day<=5:
            print(f"({is_vacation},{day}) is 7:00 AM")
    else:
            print(f"({is_vacation},{day}) is 10:00 AM")