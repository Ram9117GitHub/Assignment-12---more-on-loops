"""Write a python script to calculate LCM of two numbers"""
print("Enter two number :")
a, b = int(input()), int(input())
L=max(a,b)
while L <=  a*b:
    if L % a == 0 and L % b == 0:
        print("LCM is ",L)
        break
    L+=1


