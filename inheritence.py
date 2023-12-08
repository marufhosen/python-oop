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
