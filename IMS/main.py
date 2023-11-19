from product import Product
from transactions import Transaction
from exceptions import InvalidQuantityError, OutOfStockError, InvalidTransactionTypeError

def main():
    # Load products from CSV
    products = Product.load_products()

    # Print details of all products
    for product in products:
        print(product)

    # Create a new transaction to sell a product
    transaction = Transaction(1, products[0], 'sell', 10, '2023-11-19')

    try:
        # Execute the transaction
        transaction.execute()
    except (InvalidQuantityError, OutOfStockError, InvalidTransactionTypeError) as e:
        print(str(e))

    # Print details of all products after the transaction
    for product in products:
        print(product.get_details())

if __name__ == "__main__":
    main()
