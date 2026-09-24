#  * mutable are those which can be changed after writing 
#  * non-mutable are those which cannot be changed after writing


#  21/9/26

#  1) list() - it is known has the ordered collection of items,
#   we can create list with the help of square braces. 
#   A list can hold upto multiple values and list is a mutable values.

# flowers = ["lily", "tulip", "rose", "sunflower", "daffodil"]

# print(type(flowers))

# print(flowers[0])
# print(f"the first flower is {flowers[0]}")

# print(flowers[-1])
# print(f"the last flower is {flowers[-1]}")

# print(flowers[0:3]) # slicing 
# print(f"the first three flowers are {flowers[0:3]}")

# print(flowers[::2])  # prints alternate values
# print(flowers[::-1]) # prints the reverse order

# 23/9/26

#  2) append - adds one element at the end of the list.
#           syntax: name.append(element)


flowers = ["lily", "tulip", "rose", "sunflower", "daffodil"]

flowers.append("water lily")
print(flowers)



numbers = [1,3,5,8]

numbers.append(9)
print(numbers)

# a list can hold multiple datatypes


mix = ["pizza", "pani puri", "cake", 4 , 7 ,8]

mix.append("rice")
print(mix)


# flavour = input("enter name:")
 
# set = ["chocolate", "vanilla"]
# set.append(flavour)
# print(set)

# inp = input("enter:")

# subjects = []
# subjects.append(inp)
# print(subjects)

# lis = []
# # i = 1

# for i in range(1,11):
#     lis.append(i)
# print(lis)



lis = []
for i in range(1,6):
    name = input("enter a name:")
    lis.append(name)
print(lis)
    