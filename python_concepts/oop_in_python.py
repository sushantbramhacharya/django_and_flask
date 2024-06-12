class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f"{self.name} is {self.age} years old."

class Cat(Pet):
    def speak(self):
        return "Meow"

class Dog(Pet):
    def speak(self):
        return "Bow Bow"

my_cat = Cat("Lili", 6)
my_dog = Dog("Kali", 8)

print(my_cat.show())  
print(my_cat.speak()) 
print(my_dog.show())  
print(my_dog.speak())  
