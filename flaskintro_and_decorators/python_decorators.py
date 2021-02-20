# What exactly is a decorator?
# Well.. Let's imagine that you have a bunch of functions in your class or in your module
# and you want to add some functionality to each of these functions, well then you might
# use a decorator function to do that.
# You can think of a decorator function as a function thats going to give additional 
# functionality to an existing function.
######################
# Functions inputs/functionality/output

# def add(n1, n2):
#     return n1 + n2


# def subtract(n1, n2):
#     return n1 - n2


# def multiply(n1, n2):
#     return n1 * n2


# def divide(n1, n2):
#     return n1 / n2

# # Python Functions are First-class Objects, they can be passed around as arguments
# # e.g. just like int/string/float etc.

# def calculate(calc_function, n1, n2):
#    return calc_function(n1, n2)

# result = calculate(multiply, 2, 3)
# print(result)

# # Nested Functions
## Function can be Nested in other functions

# def outer_function():
#     print("I'm outer")

#     def nested_function():
#         print("I'm inner")

#     nested_function()

# outer_function()

## Functions can be returned from other functions

# def outer_function():
#     print("I'm outer")

#     def nested_function():
#         print("I'm inner")

#     return nested_function

# # outer_function()()
# # or
# inner_function = outer_function()
# inner_function()

## Python Decorator Function
## A function that wraps another function and gives it some additional functionality or 
## modifies the functionality.
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #^ Do something (add functionality) before
        function()
        function() #<-- or run a function twice
        #v Do something (add functionality) after
        print("test")
    return wrapper_function

@delay_decorator ##<-- syntactic sugar**
def say_hello():
    print("hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

say_hello()

# ** - Below is the @delay_decorator without the syntactic sugar

#decorated_function = delay_decorator(say_greeting)
#decorated_function()

print(say_hello)
print(delay_decorator)

function_list = [say_bye, say_greeting, say_hello]
function_list[1]()
bye = function_list[2]
bye()




















