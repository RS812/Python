class Human:
    def __init__(self,name,age,gender):
        self.name=name
        self._age=age
        self.__gender=gender
    def showmember(self):
        print("Gender is :",self.__gender)
obj=Human("Rutvi",20,"Female")
print("Name is:",obj.name)
print("Age is:",obj._age)
#print("Gender is:",obj.__gender)
obj.showmember()
