class Animal:
    def __init__(self,name):
        self.name=name
    def cansay(self,voice):
        print(f" Hello I am {self.name} and I say {voice}...")
class Dog(Animal):
    def eat(self):
        print("Dog eat's paydegree")
class Puppy(Dog):
    def walk(self):
        print("Puppy walks slowly... slowly...")
od=Dog("Dog")
od.cansay("Bhow...Bhow...")
od.eat()
od=Puppy("Puppy")
od.walk()
