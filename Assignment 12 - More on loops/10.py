""" Write a python script to calculate HCF of two numbers """
print("Enter two number :")
a,b = int(input()), int(input())
H = min(a,b)
while H>1:
    if a % H == 0 and b % H ==0 :
        print("HCF is ", H)
        break
    H -= 1