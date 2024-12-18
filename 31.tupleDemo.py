grno=(2144,2292,2216,2239,2242)
stnm=("Vishakha","Aarti","Dhanvi","Vimla","Divya")
favfood=("Ice-cream",11,35,"Burger",4.5)
print("Grno is: ",grno[0]," And Name is: ",stnm[0]," Favourite food: ",favfood[0])
i=1
for g in grno:
    print("\n GR no is :",g)
    i+=1
print("Length of the tuple is: ",i-1)
for x in range(0,i-1):
    print("Grno is: ",grno[x]," And Name is: ",stnm[x]," Favourite food: ",favfood[x])
