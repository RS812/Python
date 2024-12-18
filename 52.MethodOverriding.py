class DemoA:
     def display(self):
         print("Hello Good Morning")
class DemoB(DemoA):
    def display(self):
        super().display()
        print("I am Overriding Method")
obj=DemoB()
obj.display()
