""" Write a python script to print first N terms of a Fibonacci series """
num = int(input("Enter a number :"))
a = 1
b = 0
count =0
if num==1:
    print(a)
while count < num:
    print(b)
    sum = a+b
    a = b
    b = sum
    count+=1
