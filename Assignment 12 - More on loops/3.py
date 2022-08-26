"""Write a python script to print all Prime numbers under 100."""
print("Print all prime numbers under 100. ")
l =1
b = 100
if l>b:
    l,b = b,l
if l<1 and b >=2:
    l=2
if l < b < 2:
    pass
else:
    for i in range(l+1,b):
        for x in  range(2,i):
            if i % 2 == 0:
                break
        else:
            print(i, end=" ")
        b+=1