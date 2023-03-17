from product import Product
from beverage.beverage import Beverage

product = Product("coffee", 2.5)
print(product.__class__.__name__)
print(product.name)
print(product.price)

beverage = Beverage("coffee", 2.5, 50)
print(beverage.__class__.__name__)
print(beverage.__class__.__bases__[0].__name__)
print(beverage.name)

