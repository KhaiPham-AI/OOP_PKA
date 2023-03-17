from abc import ABC, abstractmethod


class Food(ABC):
    def __init__(self, quantity):
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass


class Vegetable(Food):
    def __str__(self):
        return f"Vegetables: {self.quantity}"


class Fruit(Food):
    def __str__(self):
        return f"Fruits: {self.quantity}"


class Meat(Food):
    def __str__(self):
        return f"Meat: {self.quantity}"


class Seed(Food):
    def __str__(self):
        return f"Seeds: {self.quantity}"
