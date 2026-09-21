#  * mutable are those which can be changed after writing 
#  * non-mutable are those which cannot be changed after writing


#  21/9/26

#  1) list() - it is known has the ordered collection of items,
#   we can create list with the help of square braces. 
#   A list can hold upto multiple values and list is a mutable values.

flowers = ["lily", "tulip", "rose", "sunflower", "daffodil"]

print(type(flowers))

print(flowers[0])
print(f"the first flower is {flowers[0]}")

print(flowers[-1])
print(f"the last flower is {flowers[-1]}")

print(flowers[0:3]) # slicing 
print(f"the first three flowers are {flowers[0:3]}")

print(flowers[::2])  # prints alternate values
print(flowers[::-1]) # prints the reverse order

# study string methods and datatypes

