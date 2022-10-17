class Shop:
    def __init__(self, name):
        self.name = name
        self.items = []

    @staticmethod
    def multiply(x, y):
        return x*y

    def add_to_cart(self, name, price, quantity):
        total = self.multiply(price, quantity)
        self.items.append((name, total))



shopno = Shop("Shopno")
shopno.add_to_cart("rice", 70, 10)
shopno.add_to_cart("potato", 40, 30)
print(shopno.multiply(1, 2))
print(shopno.items)