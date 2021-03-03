## Magic Methods / Dunder Methods

class Book():

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self): #<-- a string representation of the object
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages



b = Book('Python Rocks', 'Sam Kingston', 420)

print(len(b))
