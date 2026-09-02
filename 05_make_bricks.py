
# We want to make a row of bricks that is goal inches long.
# We have a number of small bricks (1 inch each) and big bricks (5 inches each).
# Return True if it is possible to make the goal by choosing from the given 
# bricks. This is a little harder than it looks and can be done without any loops.
# See also: Introduction to MakeBricks


# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True


small_bricks = int(input("enter a number for small bricks: "))
big_bricks = int(input("enter a number for big bricks: "))
goal = int(input("enter a number for goals: "))

print(f"({small_bricks},{big_bricks},{goal})")

if goal >= big_bricks*5:
    remaining = goal - big_bricks*5
else:
    remaining = goal%5
    
    
if small_bricks:
    print(True)
else:
    print(False)