from human import Human
class Auto:
    def __init__(self, brand = None):
        self.Brand = brand
        self.Passengers = list()
        self.Drivers = list()

    def AddPassengers(self, human):
        self.Passengers.append(human)
    def AddDrivers(self, human):
        self.Passengers.append(human)
    def ToString(self):
        print(f"Brand: {self.Brand}")