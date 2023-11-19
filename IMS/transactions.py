from product import Product
from exceptions import InvalidQuantityError, OutOfStockError, InvalidTransactionTypeError


class Transaction:
    def __init__(self, transaction_id, product, transaction_type, amount, date):
        self.transaction_id = transaction_id
        self.product = product
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = date

    def __str__(self):
        return f"Transaction ID: {self.transaction_id}\nProduct: {self.product}\nTransaction Type: {self.transaction_type}\nAmount: {self.amount}\nDate: {self.date}"

    def __repr__(self):
        return f"Transaction (ID: {self.transaction_id}, Product: {self.product}, Transaction Type: {self.transaction_type}, Amount: {self.amount}, Date: {self.date})"

    def execute(self):
        try:
            if self.transaction_type == 'sell':
                self.product.sell(self.amount)
            elif self.transaction_type == 'restock':
                self.product.restock(self.amount)
            else:
                raise InvalidTransactionTypeError(f"Invalid transaction type: {self.transaction_type}")
        except OutOfStockError:
            print("Error: Not enough products in stock.")
        except InvalidQuantityError:
            print("Error: Cannot sell or restock a negative quantity.")


