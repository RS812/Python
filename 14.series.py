n=10
a=0
b=1
for i in range(n):
    print(a,end=" ")
    tmp=a+b
    a=b
    b=tmp
