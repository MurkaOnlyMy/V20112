class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.car = None

    def assign_car(self, car):
        self.car = car

    def drive(self):
        if self.car:
            print(f"{self.name} водить автомобіль {self.car.make} {self.car.model}")
        else:
            print(f"{self.name} не має автомобіля")


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model


# Створення об'єктів класів
driver1 = Driver("Пакара", 666)
driver2 = Driver("Нікіта", 12)
car1 = Car("Toyota", "Camry")
car2 = Car("Ford", "Focus")

# Призначення автомобілів водіям
driver1.assign_car(car1)
driver2.assign_car(car2)

# Водій водить автомобіль
driver1.drive()
driver2.drive()
# Від Нікіти
