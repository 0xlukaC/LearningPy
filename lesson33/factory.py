#!/usr/bin/python3


"""
Write a Python program, factory_method.py, and demonstrate the following:
       ◦ Write a ShapeFactory class which can create shapes on demand
       ◦ Write a Shape class (which is never used directly and which will only serve as a super class) and Circle, Rectangle and Triangle classes, which will all inherit from Shape
       ◦ The shape class must have a draw() method, which the subclasses override by printing a simple message. E.g., “Drawing a circle.”
"""
# factory allows you to create objects without specifying the exact class of an object created at run time

# Concrete creators inherit from Creator which contains a create method and maybe some other method.
# The Concrete creator will override the create method to create an instance of createProduct which inherits from the product instance

"""
Product
  ↑
ConcreteProductA
ConcreteProductB

Creator
  ↑
ConcreteCreatorA
ConcreteCreatorB
"""

from abc import ABC, abstractmethod


# Product
class Shape:
    def draw(self):
        pass


# Concrete product
class CircleProduct(Shape):
    def draw(self):
        # print(f"drawing a
        # {self.name}")
        print("drawing a Circle")


class RectangleProduct(Shape):
    def draw(self):
        print("drawing a Rectangle")


class TriangleProduct(Shape):
    def draw(self):
        print("drawing a triangle")


# Creator
# class ShapeFactory(ABC):
#     @abstractmethod
#     def createShape(self) -> Shape:
#         pass


class ShapeFactory:
    def createShape(self) -> ...:
        pass


# class ShapeFactory:
#     def createShape(self):
#         raise NotImplementedError()


# Concrete creator
class Circle(ShapeFactory):
    def createShape(self):
        return CircleProduct()


class Rectangle(ShapeFactory):
    def createShape(self):
        return RectangleProduct()


class Triangle(ShapeFactory):
    def createShape(self):
        return TriangleProduct()


circle_factory = Circle()
shape = circle_factory.createShape()
shape.draw()
