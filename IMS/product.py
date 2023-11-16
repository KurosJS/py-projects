class Product:
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


class ProductStore:
    def __init__(self):
        self.store = []
        self.store_quantity = []

    def add(self, product, quantity):
        self.store.append(product)
        self.store_quantity.append(quantity)

    def set_quantity(self, product, quantity):
        for i in range(len(self.store)):
            if self.store[i] == product:
                self.store_quantity[i] = quantity

    def get_product_info(self, product):
        for i in range(len(self.store)):
            if self.store[i] == product:
                return self.store[i]

    def get_all_products(self):
        return self.store

    def get_product_quantity(self, product):
        for i in range(len(self.store)):
            if self.store[i] == product:
                return self.store_quantity[i]

    def get_store_info(self):
        for i in range(len(self.store)):
            print(self.store[i], self.store_quantity[i])

    def __str__(self):
        return "Store: " + str(self.store) + " Store quantity: " + str(self.store_quantity)


class Customer:
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_phone(self):
        return self.phone

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname

    def set_phone(self, phone):
        self.phone = phone

    def __str__(self):
        return "Name: " + self.name + " Surname: " + self.surname + " Phone: " + self.phone


class Order:
    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = quantity

    def get_customer(self):
        return self.customer

    def get_product(self):
        return self.product

    def get_quantity(self):
        return self.quantity

    def set_customer(self, customer):
        self.customer = customer

    def set_product(self, product):
        self.product = product

    def set_quantity(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return "Customer: " + str(self.customer) + " Product: " + str(self.product) + " Quantity: " + str(self.quantity)


class OrderStore:
    def __init__(self):
        self.store = []

    def add(self, order):
        self.store.append(order)

    def get_order_info(self, order):
        for i in range(len(self.store)):
            if self.store[i] == order:
                return self.store[i]

    def get_all_orders(self):
        return self.store

    def get_orders_by_customer(self, customer):
        for i in range(len(self.store)):
            if self.store[i].get_customer() == customer:
                print(self.store[i])

    def get_orders_by_product(self, product):
        for i in range(len(self.store)):
            if self.store[i].get_product() == product:
                print(self.store[i])

    def get_orders_by_customer_and_product(self, customer, product):
        for i in range(len(self.store)):
            if self.store[i].get_customer() == customer and self.store[i].get_product() == product:
                print(self.store[i])

    def __str__(self):
        return "Store: " + str(self.store)


class Report:
    def __init__(self, order_store, product_store):
        self.order_store = order_store
        self.product_store = product_store

    def get_income_by_order(self, order):
        for i in range(len(self.order_store.store)):
            if self.order_store.store[i] == order:
                return self.order_store.store[i].get_product().get_price() * self.order_store.store[i].get_quantity()

    def get_income_by_store(self):
        income = 0
        for i in range(len(self.order_store.store)):
            income += self.order_store.store[i].get_product().get_price() * self.order_store.store[i].get_quantity()
        return income

    def get_income_by_product(self, product):
        income = 0
        for i in range(len(self.order_store.store)):
            if self.order_store.store[i].get_product() == product:
                income += self.order_store.store[i].get_product().get_price() * self.order_store.store[i].get_quantity()
        return income

    def get_income_by_customer(self, customer):
        income = 0
        for i in range(len(self.order_store.store)):
            if self.order_store.store[i].get_customer() == customer:
                income += self.order_store.store[i].get_product().get_price() * self.order_store.store[i].get_quantity()
        return income

    def get_income_by_period(self, start_date, end_date):
        income = 0
        for i in range(len(self.order_store.store)):
            if start_date <= self.order_store.store[i].get_date() <= end_date:
                income += self.order_store.store[i].get_product().get_price() * self.order_store.store[i].get_quantity()
        return income

    def get_income_by_product_and_period(self, product, start_date, end_date):
        income = 0
        for i in range(len(self.order_store.store)):
            if self.order_store.store[i].get_product() == product and start_date <= self.order_store.store[i].get_date() <= end_date:
                income += self.order_store.store[i].get_product().get_price() * self.order_store.store[i].get_quantity()
        return income

    def get_income_by_customer_and_period(self, customer, start_date, end_date):
        income = 0
        for i in range(len(self.order_store.store)):
            if self.order_store.store[i].get_customer() == customer and start_date <= self.order_store.store[i].get_date() <= end_date:
                income += self.order_store.store[i].get_product().get_price() * self.order_store.store[i].get_quantity()
        return income

    def get_income_by_customer_and_product_and_period(self, customer, product, start_date, end_date):
        income = 0
        for i in range(len(self.order_store.store)):
            if self.order_store.store[i].get_customer() == customer and self.order_store.store[i].get_product() == product and start_date <= self.order_store.store[i].get_date() <= end_date:
                income += self.order_store.store[i].get_product().get_price() * self.order_store.store[i].get_quantity()
        return income




product_store = ProductStore()
product_store.add(Product("Apple", 100, 10), 10)
product_store.add(Product("Banana", 200, 20), 20)
product_store.add(Product("Orange", 300, 30), 30)
product_store.add(Product("Pineapple", 400, 40), 40)

customer1 = Customer("Ivan", "Ivanov", "111111")

order_store = OrderStore()
order_store.add(Order(customer1, product_store.get_all_products()[0], 5))
order_store.add(Order(customer1, product_store.get_all_products()[1], 10))
order_store.add(Order(customer1, product_store.get_all_products()[2], 15))

report = Report(order_store, product_store)

print(report.get_income_by_order(order_store.get_all_orders()[0]))
print(report.get_income_by_store())
print(report.get_income_by_product(product_store.get_all_products()[0]))