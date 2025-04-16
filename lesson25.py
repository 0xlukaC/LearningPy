#!/home/lukachalker/myenv/bin/python3

"""
◦ Research and explain the Python mechanic of ‘name mangling’
      ◦ Research and explain the difference between public, protected and private fields/methods in OOP
  • Write a Python program, product.py, and demonstrate the following:
      ◦ Create a Product class with the following attributes:
          ▪     name (public) – the name of the product.
          ▪     __price (private) – the price of the product.
          ▪     __quantity (private) – the available quantity of the product.
      ◦ The class should have:
          ▪     A method get_details() to return a formatted string with the product's name, price, and quantity.
          ▪     A setter method set_price() that updates the product price, but only if the price is a positive value.
          ▪     A setter method set_quantity() that updates the quantity, but only if the quantity is a non-negative integer.
          ▪     A getter method get_price() to retrieve the price and get_quantity() to retrieve the quantity.
"""

"""
Name mangling is a tool where identifiers with double underscores are internally changed within the interpreter to include the class name.
This helps avoid naming conflicts in subclasses but does not make the variable truly private.

Public: accessible from anywhere.

_Protected: a convention indicating it should only be accessed within the class and subclasses.

__Private: triggers name mangling to restrict access from outside the class, intended for internal use only.
"""


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price
        self.__quantity = quantity

    def getDeets(self):
        return f"name, price and quantity, respectively {self.name}, {self.__price}, {self.__quantity}"

    def set_price(self, price):
        # self.__price = price if price else None
        self.__price = price if price is not None else None

    def set_quantity(self, quantity):
        self.__quantity = quantity if quantity is not None else None

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__price
