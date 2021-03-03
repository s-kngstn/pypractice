class NameOfClass():
    # Functions seen below are called methods when inside of a class/object
    def __init__(self, param1, param2): #__init__ allows us to create instances of the object
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        # Perform some action
        print(self.param1)

