from animal import Mammal


class Mouse(Mammal):
    allowed_food = ("Vegetables", "Fruits")
    weight_per_food = 0.10

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    allowed_food = "Meat"
    weight_per_food = 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    allowed_food = ("Vegetables", "Meat")
    weight_per_food = 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    allowed_food = "Meat"
    weight_per_food = 1.00

    def make_sound(self):
        return "ROAR!!!"

