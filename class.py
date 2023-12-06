# A SIMPLE CLASS
class Bike:
    # --init-- is a CONSTRUCTOR
    def __init__(self, name, brand, origin):
        self.bike_name = name
        self.brand_name = brand
        self.origin = origin

    # A METHOD
    def show(self):
        print(
            f"{self.bike_name} is a {self.brand_name} company's bike & origin {self.origin}"
        )


# CREATE OBJECT
bike1 = Bike("Suzuki Gixxer FI ABS", "Suzuki", "Japan")
bike2 = Bike("Pulsure N150", "Bajaj", "India")


bike1.show()
bike2.show()

# OUTPUT
# Suzuki Gixxer FI ABS is a Suzuki company's bike & origin Japan
# Pulsure N150 is a Bajaj company's bike & origin India

"""Make another class to create object"""


class Phone:
    def __init__(self, name, model):
        self.phone_name = name
        self.model = model

    def details(self):
        pf = self.phone_name
        md = self.model
        print(f"{pf} {md}")


phone1 = Phone("Realmi", "GT1")
phone1.details()

# OUTPUT
# Realmi GT1
