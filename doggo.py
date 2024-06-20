class Dog:
    def __init__(self, name, age, size):
        self.name = name
        self.age = age
        self.size = size

    def likes_walks(self):
        return True
    
    def walking_speed(self):
        return "Walk"
    
class Poodle(Dog):
    def __init__(self, name, age, size):
        super().__init__(name, age, size)

    def low_alergen(self):
        return "Yes"

    def walking_rate(self):
        return "Walk"
            
class Labrador(Dog):
    def __init__(self, name, age, size):
        super().__init__(name, age, size)

    def temperament(self):
        if self.age < 2:
            return "Flighty"
        elif self.age <10:
            return "Fun Loving"
        else:
            return "Getting slower"
        
    def walking_speed(self):
        return "Run"
       
class LabraDoodle(Poodle,Labrador):
    def __init__(self, name, age, size):
        super().__init__(name, age, size)

    def walking_rate(Labrador):
        return "Run"
   
bob = Poodle('Bob', 2, 'small')
print(bob.name, bob.age, bob.size)
print(bob.likes_walks())

swiftie = LabraDoodle('Swiftie', 1, "Medium")
print(swiftie.low_alergen())
print(swiftie.temperament())

print(bob.walking_speed())
print(swiftie.walking_speed())

basic_doggo = Dog('Henry', 4, 'Large')
print(basic_doggo.walking_speed())
