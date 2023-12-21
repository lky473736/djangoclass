class Dog :
    dog = 'dog'
    
    def __init__ (self, name, breed) :
        self.name = name
        self.breed = breed

hans = Dog("Hans", "German Shepherd")
lou  = Dog("Lou", "Labrador")
print(f"{hans.name} and {lou.name} are friends")