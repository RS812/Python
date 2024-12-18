try:
    first=int(input("Enter First Number:"))
    second=int(input("Enter Second Number:"))
    print("Division is:", (first/second ))
except Exception as e:
    print("Ooppsss there is something wrong")
    print(e)
