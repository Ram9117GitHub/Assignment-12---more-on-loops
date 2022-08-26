"""Write a python script to check whether a given pair of numbers are co-Prime numbers or not."""
print("Enter two number :")
a,b = int(input()), int(input())
H = min(a,b)
while H>1:
    if a % H == 0 and b % H == 0:
        if H == 1:
            print("Co-prime number")
    else:
        print("Not")
        break
    H-=1