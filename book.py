#!/home/lukachalker/myenv/bin/python3

"""
What is a class? What is an object? Explain with an example
    A class is a blueprint for an object and an object is a datastructure that holds data and actions that it can preform. Example is the code below

How does the __init__ method work in Python classes?
    its a constructor

What is the purpose of the self keyword in class methods?
    refers to the object/class itself
"""


"""
Create a class Book with attributes title and author
Add a method get_info() that returns the string "Title: <title>, Author: <author>"
Create two book objects and print their details using get_info()
"""


class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

    def get_info(self):
        print(f"Title: {self.title}, Author: {self.author}")


book1 = Book("1984", "george")
book2 = Book("crime and punishment", "Dostoevsky")

book1.get_info()
book2.get_info()
