LST=[]
for v in range(0,5):
    data=int(input("Enter Number :"))
    LST.insert(v,data)
print("Create List is: ",LST)
#LST.get()
LST.insert(3,100)
print("Modified List:",LST)
LST.remove(100)
print("Modified List:",LST)
#LST.removeAt(2)
#print("Modified List:",LST)
