# Basics of Python

print("Welcome to ML journey")

#variable assignment
name = "Vanshika"
age = 19

a = 2
b = 3.14
c = "vanshika"
d = True
e = 10; f = 3.14; g = "abc"
e, f, g = 10, 3.14, "abc"
h = i = j = 7
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#python has 33 keywords

#arithmetic operators
a = 4/2 #performs true division and yields float 2.0
b = 7%2 #% yields remainder 1
c = 2**4 # 2 raised to power 4
d = 4//3 # // yields quotient after discarding fractional part also called floor division

print(a)
print(b)
print(c)
print(d)

e **= 3 # same as e = e**3
f %= 10 # b = b%10

#floor division - result is the largest integer which is less than or equal to quotient
print(10//3) #3
print(-10//3) # -4
print(10//-3) # -4
print(-10//-3) #3
print(3//10) #0
print(3//-10) #-1
print(-3//10) #-1
print(-3//-10) #0

# precedence - PEMDAS( parentheses, exponentation, multiply, divide, add, sub)
# type conversions
print(int(2.14)) # from float/numeric string to int
print(float(3))
print(complex(8))
print(complex(8.0))
print(bool(4))
print(str(78))
print(chr(8)) # yields character corresponding to int

#built-in functions
print(pow(2,2))
print(min(4,5,6,7))
print(max(4,5,6,7))
print(round(893.9808, 2)) # returns x rounded to n digits after
print(bin(23))
print(oct(23))
print(hex(23))

#built- in math modules - math, cmath, random, decimal

import math
import random
print(math.factorial(7))
print(math.degrees(math.pi))
print(random.random())