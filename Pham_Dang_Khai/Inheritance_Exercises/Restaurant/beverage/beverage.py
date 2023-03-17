from B7.B7_b5.product import Product

class Beverage(Product):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price)
        self.__milliliters = milliliters

    def milliliters(self):
        return self.__milliliters