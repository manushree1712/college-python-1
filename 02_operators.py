# # 25 august 2026

# #arthematic operators
# # +,-,*,/,//,%,**


print(70+9)
print(70-9)
print(70*9)
print(70/9)
print(70//9)
print(-70//9)
print(70%9)
print(70**9)

# #comparison operators
# #compares two numbers

print(90>6)
print(-1<-5)
print("sun">"moon")
print("a">"b")    #alphabets - a is smallest and z is greatest and they skip words if they have same letters atmost
print("Earth"<"earth") #capital alphabets are smaller than normal alphabets


# logical operators
# and, or, not


x = 6
y = 4

print(x<10 or y>2) #1,1
print(x>5 or y<2) #1,0

print(x>4 and y>3) #1,1
print(x<5 and y>2) #0,1

#print(x<10 or z>5) #kind of error with or; 1,0
# print(x<2 or z<2) #kind of error with or; 0,0 - error

#print(y>2 and z<4) # error with and; 1,0
#print(x<5 and z>3) #error with and: 1,0

print(not x>5)
print(not y>10)

t = 0
print(not t)


# #assignment operators
# #=, +=, -=, *=, /=, //=, **=, %=

k = 7
k+= 9
k*=4
k/=8
print(k)  # these go step by step instead of individual


p = "h"
p+= "e"
p+= "l"
p+= "l"
p+= "o"
p+= " "
p+= "g"
p+= "u"
p+= "y"
p+= "s"
print(p)

#walrus operator

x=6
print(x>3)

print(x:=6>3)

# bitwise operators

# 2^0 = 1, 2^1 = 2, 2^2 = 4..... in book