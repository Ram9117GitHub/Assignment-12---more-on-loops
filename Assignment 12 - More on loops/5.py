""""Write a python script to find next prime number of a given number"""
num = int(input("Enter a number: "))
n = num + 1
while True:
    for i in range(2,n):
        if num % i == 0:
            break
    else:
        print("Next prime number is ",num)
        break
    num +=1

