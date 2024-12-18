Python=int(input ("Enter marks of Python:"))
J2EE=int(input ("Enter marks of J2EE:"))
CS=int(input ("Enter marks of CS:"))
total=Python+J2EE+CS
print("Total =",total)
p=(total)/3
print("Percentage=",p)
if Python<=27 or J2EE<+27 or CS<=27:
    print("Result is Fail")
else:
    print("Result is pass")
if(p>=90):
    print("Grade :A")
elif p>=80 and p<90:
    print("Grade :B")
elif p>=70 and p<80:
    print("Grade :C")
elif p>=60 and p<70:
    print("Grade :D")
else:
    print("Grade :E")
