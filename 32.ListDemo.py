LST1=[1,2,3,4,5,6,7,8,9,0]
LST2=['a','b','c','d','e']
print("First List Data:")
print("*"*40,end='\n')
for v in LST1:
    print(v,end=' ')
print("\n Second List Data:")
print("*"*40,end='\n')
for v in LST2:
    print(v,end=' ')
print("\n Length of the List1:",len(LST1))
LST1.append(3)
print("First List Data using index")
print("*"*40,end='\n')
for v in range(0,len(LST1)):
    print(LST1[v],end=' ')
#print("Comparison:",cmp(LST1,LST2))
LST1.reverse()
print("\n Reverse List:",LST1)
print("Count:",LST1.count(3))
LST1.insert(1,10)
print("New List",LST1)
