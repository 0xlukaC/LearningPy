#!/home/lukachalker/myenv/bin/python3

"""
• Write a text file, inheritance.txt, and answer the following:
  Answer in 3-4 bullet points for each of these points:
    ◦ What is the difference between inheritance and polymorphism in Python?
    ◦ How does method overriding work in polymorphism?
• Write a Python program, inheritance.py, and demonstrate the following:
    ◦ Create a parent class Vehicle with a method start_engine()
    ◦ Create a child class Car that inherits from Vehicle and overrides the start_engine() method to print a message specific to cars
    ◦ Create another child class Motorcycle that inherits from Vehicle and overrides the start_engine() method to print a message specific to motorcycles
    ◦ Use the parent class and polymorphism to call the start_engine() method on both Car and Motorcycle objects
• Write a Python program, super.py, and demonstrate the following:
    ◦ Create a parent class Person with an __init__ method that initialises the name attribute
    ◦ Create a child class Student that inherits from Person, and uses super() to initialize the name attribute and adds a student_id and grade attributes
    ◦ Instantiate an object of Student and print its name, student_id  and grade

"""


"""
- In inheritance, a class (child) inherits attributes and methods from another class (parent). this promotes code reuse
- polymorphism is using the same method/interface accross different classes, where each class can define its own version of the method/interface

- Method overriding enables polymorphism by allowing a subclass to provide its own version of a method defined in the parent class.
"""


class Vehicle:
    def __init__(self):
        pass

    def startEngine(self):
        pass


class Motorcycle(Vehicle):
    def __init__(self):
        pass

    def startEngine(self):
        print("motocycle has started and crashed immediately")


vehicles = [Vehicle(), Motorcycle()]

for v in vehicles:
    v.start_engine()


class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, id, grade):
        super().__init__(name)
        self.id = id
        self.grade = grade


s = Student("goge", "S123", "A")
print(s.name, s.id, s.grade)
