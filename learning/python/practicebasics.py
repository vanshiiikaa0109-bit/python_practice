#check whether all are digits
c = "132472332637"
print(c.isdigit())

#wap that makes use of functions in math module
# study about ceil, floor, trunc

import math
import random
x = 4
print(math.pi, math.e)
print(math.sqrt(x))
print(math.factorial(x))
print(math.log(x))

#wap to swap value of a and b. not allowed to use third variable and perform arithmetic on a and b

a = 10
b = 12
print("before swapping:")
print(a)
print(b)

a, b = b, a
print("after swapping:")
print(a)
print(b)

#wap that generates 5 random numbers in the range 10 to 50 seed value = 6
import random
random.seed(6) # sets seed value so that same random value is generated all time

for i in range(5):
    print(random.randint(10,50))

#fahernheit to centigrades

f = 98.6
c = (5 / 9) * (f - 32)
print(c)

f = float(input("write temperature in fahernheit"))
c = (5 / 9) * (f - 32)
print("faherneit temperature in celsius is" ,c)

#three sides of triangle a,b,c 
import math

a = float(input("enter first side"))
b = float(input("enter second side"))
c = float(input("enter third side"))

cosA = (b**2 + c**2 - a**2) / (2 * b * c)

A = math.degrees(math.acos(cosA))
print(A)

#print imaginary part
x = 2 + 3j
print(x.imag)

#conjugate
x = 2 + 3j
print(x.conjugate())

#float to numeric string
print(str(4.33))

#binary to decimal
binary = "1100001110"
decimal = int(binary, 2)
print(decimal)

#obtaining quotient and remainder when dividing 29 with 5
print(29%5) #remainder
print(29//5) #quotient

print(hex(34567))

print(round(45.6782, 2))

#obtain 4 from 3.556

import math
print(math.ceil(3.556))

#obtain 17 from 16.7844

import math
print(math.ceil(16.7844))

#obtain remainder
print(3.45% 1.22)