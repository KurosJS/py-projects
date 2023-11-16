class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def set_quantity(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return "Name: " + self.name + " Price: " + str(self.price) + " Quantity: " + str(self.quantity)