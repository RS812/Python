class Animal:
   def __init__(self,name):
       self.name=name
   def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print(f" {self.name} ...says Bhow ...Bhow...")
class Puppy(Animal):
    def speak(self):
        print(f"{self.name} ...says Bow... Bow...")
dog=Dog("Dog")
puppy=Puppy("Puppy")
dog.speak()
puppy.speak()
