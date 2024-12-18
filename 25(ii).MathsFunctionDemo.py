import MyMaths
a=int(input("Enter First Value:"))
b=int(input("Enter Second Value:"))
print("Addition is :",MyMaths.Addition(a,b))
print("Subtraction is :",MyMaths.Subtraction(a,b))
print("Multiplication is :",MyMaths.Multiplication(a,b))
print("Division is :",MyMaths.Division(a,b))
print("Modulus is :",MyMaths.Modulus(a,b))
print("Power is :",MyMaths.Power(a,b))
print("Absolute is:",MyMaths.Absolute(a))
print("Square is :",MyMaths.Square(a,b))
print("Cube is:",MyMaths.Cube(a,b))
print("Multiplication Table is: ")
a=8
for i in range (1,11):
    print(a, 'x' , i, '=' ,a*i)

