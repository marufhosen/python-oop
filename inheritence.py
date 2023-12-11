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


# ANOTHER EXAMPLE--------------------


# BASE CLASS / SUPER CLASS
class Polygon:
    def __init__(self, no_of_sides):
        self.no = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def take_input(self):
        self.sides = [
            float(input(f"Input value for no {i+1}: ")) for i in range(0, self.no)
        ]

    def view(self):
        for i in range(self.no):
            print(f"Side {i+1} is: {self.sides[i]}")


# DERIVE CLASS / CHILD CLASS


class Triangle(Polygon):
    # def __init__(self, no_of_sides):
    #     super().__init__(no_of_sides)
    def __init__(self):
        Polygon.__init__(self, 3)

    def area(self):
        side1, side2, side3 = self.sides
        s = (side1 + side2 + side3) / 2
        area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
        print(f"Each sides of triangle: {side1}, {side2}, {side3}")
        print(f"Area of this triangle is: {area}")


# res = Polygon(3)
# res.take_input()
# res.view()

res2 = Triangle()
res2.take_input()

res2.area()
