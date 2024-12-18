class Animal:
    def cansay(self):
        print(f" Hello I am  from animal class")
class Dog(Animal):
    def eat(self):
        print("Dog eat's paydegree")
class Puppy(Animal):
    def walk(self):
        print("Puppy walks slowly... slowly...")
class Bird(Dog,Puppy):
    def fly(self):
        print("Bird can fly in sky")

Bird=Bird()
Bird.cansay()
Bird.eat()
Bird.walk()
Bird.fly()
