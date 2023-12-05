# A SIMPLE CLASS

class Bike:
    # --init-- is a CONSTRUCTOR
    def __init__(self, name, brand, origin):
        self.bike_name = name
        self.brand_name = brand
        self.origin = origin

    def Show(self):
        print(f"{self.bike_name} is a {self.brand_name} company's bike & origin {self.origin}")


bike1 = Bike("Suzuki Gixxer FI ABS", "Suzuki", "Japan")
bike2 = Bike("Pulsure N150", "Bajaj", "India")

# print(bike1)
# print(bike2)

bike1.Show()
bike2.Show()
