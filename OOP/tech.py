class Tech(object):    def __init__(self, name: str, price):        self.name = name        self.price = price    def product(self):        items = f"The product name is: {self.name}\nThe product price is: {self.price}"        return itemsmy_tech = Tech("Laptop", 2340)print(my_tech.product())