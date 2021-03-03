# Everything in Python is an Object 
# Classes are User Defined Objects

class Dog():

    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal' # <-- Always the same, regardless of the instance of Dog()

    def __init__(self, breed, name): #<-- Required positional argument
        # USER DEFINED ATTRIBUTES
        # Required attributes to define the Dog class
        self.breed = breed
        self.name = name

    # Methods are functions defined in the body of a class that are used to perform
    # operations that sometimes utilize the actual attributes of the object we created.
    # " Functions acting on an object that take the object itself into account through the use of the
    # self argument/keyword. "
    # OPERATIONS/Actions --->  Methods
    def bark(self, number):
        print(f"WOOF my name is {self.name}, your number is {number}")



my_dog = Dog(breed='German Shepard', name='Buddy') # <--- instance of a class

print(type(my_dog)) # <------ __main__.Dog

print(my_dog.breed) # <--- 'Pitbull'
print(my_dog.name)
print(my_dog.species) # <-- always 'mammal'
my_dog.bark(4) # <-- Performs the method above when called with the dog instance my_dogs

class Circle():
    # Class Object Attribute
    # Something that is True for any instance of the class
    pi = 3.14

    def __init__(self, radius=1): #<-- default radius value, but can be changed / overwritten
        
        self.radius = radius
        self.area = radius*radius*Circle.pi

    # METHOD
    def get_circumference(self):
        return self.radius * Circle.pi * 2 #<- using Circle.pi makes it clear that its a
                                            # Class Object Attribute being used and not a 
                                            # user defined attribute.

my_circle = Circle(radius=30)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.area)
print(my_circle.get_circumference())





