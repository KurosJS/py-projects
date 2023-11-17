import csv

class Product:
    FILENAME = 'products.csv'

    def __init__(self, product_id, name, price, quantity, description):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    def __str__(self):
        return f"Product: {self.name}, price: {self.price}, quantity: {self.quantity}"

    def rest(self, quantity):
        self.quantity += quantity
        self._update_csv()

    def sell(self, quantity):
        if self.quantity - quantity < 0:
            raise Exception("Not enough products in stock")
        self.quantity -= quantity
        self._update_csv()

    def _update_csv(self):
        with open(Product.FILENAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        for row in rows:
            if int(row['Product ID']) == self.product_id:
                row['Quantity'] = str(self.quantity)

        with open(Product.FILENAME, mode='w', newline='') as file:
            fieldnames = ['Product ID', 'Name', 'Price', 'Quantity', 'Description']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    @staticmethod
    def load_products():
        products = []
        with open(Product.FILENAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product = Product(int(row['Product ID']), row['Name'], float(row['Price']), int(row['Quantity']), row['Description'])
                products.append(product)
        return products

    def get_total_sum(self):
        return self.quantity * self.price

    def get_details(self):
        return f"Name: {self.name}, price: {self.price}, quantity: {self.quantity}, description: {self.description}"
