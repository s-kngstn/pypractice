# Inheritance & Polymorphism
# Inheritance is a way to form new classes using classes that have already been defined.
# Benefits of Inheritance = Ability to reuse code that youve already worked on.
# Benefits of Inheritance = Reduce complexity of a program.

class Animal():

    def __init__(self):
        print("ANIMAL CREATED")
    
    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

myanimal = Animal()
myanimal.eat()
myanimal.who_am_i()

# class Dog(Animal):

#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog Created")
    
#     def who_am_i(self):
#         print("I am a dog")

#     def bark(self):
#         print("wooof woooffff")

# mydog = Dog()
# mydog.eat()
# mydog.who_am_i()
# mydog.bark()

# Polymorphism refers to the way which different object classes can share the same method name, and
# then those methods can be called from the same place even though a variety of different Objects
# be passed in.

class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"

class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"


niko = Dog("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())

for pet_class in [niko,felix]:

    print(type(pet_class))
    print(pet_class.speak())

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
