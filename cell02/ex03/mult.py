#!/usr/bin/env python3
a = float(input("Enter the first number: \n"))
y = float(input("Enter the second number: \n"))
print( a, "x", y, "=", a*y)
x = float(a*y)
x = int(x)
if x == 0 :
    print("This number is both positive and negative")
elif x < 0 :
    print("This number is negative.")
else :
    print("This number is positive.")