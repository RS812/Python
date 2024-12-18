try:
    first=int(input("Enter First Number:"))
    second=int(input("Enter Second Number:"))
    print("Division is:", (first/second ))
except IOError:
    print("Input Proper Data..")
except ZeroDivisionError:
    print("Zero not divided by value.")
except Exception as e:
    print("Error is:",e)
finally:
    print("Thank you for Executing code..")
