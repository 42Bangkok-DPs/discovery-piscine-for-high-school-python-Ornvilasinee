#!/usr/bin/env python3
num=int(float(input("Enter a number less than 25 \n")))
if num <= 25 :
    i=num
    while i <= 25 :
        print("Inside the loop, my variable is", i)
        i +=1
else :
    print("Error")