def series1(N,v):
    if(N==v):
        return N
    else:
        return str(N)+" "+str(series1(N+1,v))
n=int(input("Enter n no. value:"))
print(" ",series1(1,n))