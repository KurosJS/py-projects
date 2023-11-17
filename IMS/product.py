class Product:
    def __init__(self, product_id, name, price, quantity, description):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    def __str__(self):
        return f"Product: {self.name}, price: {self.price}, quantity: {self.quantity}"

    def __repr__(self):
        return f"Product: {self.name}, price: {self.price}, quantity: {self.quantity}"

    def rest(self, quantity):
        self.quantity += quantity

    def sell(self, quantity):
        if self.quantity - quantity < 0:
            raise Exception("Not enough products in stock")
        self.quantity -= quantity

    def get_total_sum(self):
        return self.quantity * self.price

    def get_details(self):
        return f"Name: {self.name}, price: {self.price}, quantity: {self.quantity}, description: {self.description}"


banana = Product(1, "banana", 20, 100, "yellow")
apple = Product(2, "apple", 30, 200, "green")
orange = Product(3, "orange", 40, 300, "orange")

print(banana)
print(apple)
print(orange)

print(banana.get_total_sum())
print(apple.get_total_sum())
print(orange.get_total_sum())

banana.sell(10)
apple.sell(20)
orange.sell(30)

print(banana)
print(apple)
print(orange)

print(banana.get_total_sum())
print(apple.get_total_sum())
print(orange.get_total_sum())

banana.rest(10)
apple.rest(20)
orange.rest(30)

print(banana)
print(apple)
print(orange)

print(banana.get_total_sum())
print(apple.get_total_sum())
print(orange.get_total_sum())

print(banana.get_details())
print(apple.get_details())
print(orange.get_details())





