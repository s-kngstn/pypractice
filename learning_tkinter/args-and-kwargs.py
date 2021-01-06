# Advanced Python Arguments
# Unlimited positional arguments - *args
def add(*args):
    total = 0
    for num in args:
        total += num
    return total


# *args basically packs all the values into a tuple
answer = add(2, 5, 7, 9)
print(add(200, 3))  # prints 203
print(answer)  # prints 23


# Keyword Arguments - *kwargs
def calculate(n, **kwargs):
    print(kwargs)
    #     for key, value in kwargs.items():
    #         print(key)
    #         print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# **kwargs is a dictionary
calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.year = kwargs.get("year")
        self.seats = kwargs.get("seats")


# using .get() instead of ["keyword"] has its benefits:
# if this key doesnt exist in the dictionary, then it will just return
# none and it wont give us an error.
my_car = Car(make="Tesla", model="Roadster")
print(my_car.make)
