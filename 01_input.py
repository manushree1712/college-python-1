# 24 august 2026


x = int(input("enter x: "))
y = int(input("enter y: "))
print(x + y)


a = float(input("enter a: "))
b = float(input("enter b: "))
print(a + b)


l = int(input("enter length: "))
b = int(input("enter breadth: "))
area = l*b
print("area of rectangle:", area)


r = int(input("enter radius: "))
area_of_circle = 3.14*r*r
print("area of circle:", area_of_circle)
print(f"area of circle: {area_of_circle:.3f}")


name = input("enter name:")
print("good morning,", name)
print(f"good morning, {name}")



# add 2 numbers x and y and print its square root

x = int(input("enter number 1:"))
y = int(input("enter number 2:"))

result = (x+y)**(0.5)

print(f"the result of {x} and {y} is {result:.3f}")
