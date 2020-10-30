class Computer:

    def __init__(self):
        self.name = "MacBook Air"  # Public
        self.__maxprice = 90000  # Protected
        self._budget = 80000  # Private

    def sell(self):
        print(f"Selling Price: {self.__maxprice}")

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()

c._budget = 95000
print(c._budget)

c.__maxprice = 120000
print(c.__maxprice)
