from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food):
        if not isinstance(food, self.allowed_food):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += self.weight_per_food * food.quantity
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight:.2f}, {self.food_eaten}]"


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region


