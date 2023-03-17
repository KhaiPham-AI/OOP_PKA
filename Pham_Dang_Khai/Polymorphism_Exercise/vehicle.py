from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
        self.fuel_consumption += 0.9

    def drive(self, distance):
        required_fuel = distance * self.fuel_consumption
        if required_fuel <= self.fuel_quantity:
            self.fuel_quantity -= required_fuel
            return True
        else:
            return False

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
        self.fuel_consumption += 1.6

    def drive(self, distance):
        required_fuel = distance * self.fuel_consumption
        if required_fuel <= self.fuel_quantity:
            self.fuel_quantity -= required_fuel
            return True
        else:
            return False

    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)