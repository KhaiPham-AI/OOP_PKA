from animal import Bird


class Owl(Bird):
    allowed_food = "Meat"
    weight_per_food = 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    allowed_food = ("Vegetables", "Fruits", "Meat", "Seeds")
    weight_per_food = 0.35

    def make_sound(self):
        return "Cluck"


