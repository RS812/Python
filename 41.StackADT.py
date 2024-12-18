stack=[]
for v in range(0,5):
    data=int(input("Enter Number :"))
    stack.append(data)
print("Create stack is: ",stack)
print("Popped value is:",stack.pop())
print("Modified stack:",stack)
print("Popped value is:",stack.pop())
print("Popped value is:",stack.pop())
print("Popped value is:",stack.pop())
print("Popped value is:",stack.pop())
print("Modified stack:",stack)
stack.append(100)
print("Modified stack:",stack)
