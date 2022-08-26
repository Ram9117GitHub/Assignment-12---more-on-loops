"""Write a python script to print first N prime numbers."""
num = int(input("Enter a number :"))
for e in range(2,num+1):
    for i in range(2,e):
        if e % i == 0:
            break
    else:
        print(e)