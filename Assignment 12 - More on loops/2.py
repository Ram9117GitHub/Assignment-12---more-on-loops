"""Write a python script to check whether a given number is Prime or not"""
print("---------------------------------------------------------------------------------------------------------")
num = int(input("Enter a number :"))
if num==2:
    print("prime number")
elif num % 2 == 1:
        print("Prime number")
else:
    print("Not Prime number")
print("------------------------------------------------------------------------------------------------------------")
num = int(input("Enter a number :"))
if num<2:
    print("Not a prime number")
else:
    for i in range (2, num):
        if num % 2 == 0 :
            print("Prime not")
            break
    else:
        print("Prime number")
print("---------------------------------------------------------------------------------------------------------------")