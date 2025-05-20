#!/usr/bin/python3


# Product
class Shape:
    def draw(self):
        raise NotImplementedError()


# ConcreteProducts
class Circle(Shape):
    def draw(self):
        print("Drawing a Circle.")


class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle.")


class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle.")


# Creator (Factory)
class ShapeFactory:
    def createShape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        elif shape_type == "triangle":
            return Triangle()
        else:
            raise ValueError("Unknown shape type")


# Client code
factory = ShapeFactory()

shape1 = factory.createShape("circle")
shape1.draw()

shape2 = factory.createShape("rectangle")
shape2.draw()
