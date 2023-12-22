class Animal :
    def __init__ (self, name, species) :
        self.name = name
        self.species = species
        
    def greet (self) :
        print (f"Hi! My name is {self.name} and I am a {self.species}")
        
class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Dog")
    def sound(self):
        print("Wuff")
    
class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Cat")
    def sound(self):
        print("Meow")