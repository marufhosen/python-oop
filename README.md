# python-oop
 [DOCS](https://docs.google.com/document/d/1-VLEITIf2c82nzraZ6UXPtXDi0HtlIosKMxoz3A3mKc/edit#heading=h.5t3i6qd0go1s)

#### Class: Class is a machine to generate instance/object.

#### Method: A method like a python function
    1. Must be call on an object.
    2. Must be put it inside the class.
    3. A method has a name, it take parameters and able to return statement.


# Object oriented programming(OOP) stands on four piller.
    1. Inheritance.
    2. Encapsulation.
    3. Polymorphism.
    4. Abstraction.


### Python Inheritance
Inheritance is a way of creating a new class for using details of an existing class without modifying it.

# Examples

```python
# BASE/PARENT CLASS
class Animal:
    def __init__(self):
        pass

    def eat(self):
        print("I can eat!")

    def sleep(self):
        print("I can sleep")

# DERIVE/CHILD CLASS
class Dog(Animal):
    def __init__(self):
        pass

dog = Dog()
dog.eat()
dog.sleep()
```