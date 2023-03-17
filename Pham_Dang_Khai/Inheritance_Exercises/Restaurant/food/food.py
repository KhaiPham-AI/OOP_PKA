from B7.B7_b5.product import Product

class Food(Product):
    def __init__(self, name, price, grams):
        super().__init__(name, price)
        self.__grams = grams

    def get_grams(self):
        return self.__grams