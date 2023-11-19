class OutOfStockError(Exception):
    """Raised when trying to sell more products than are in stock."""
    pass

class InvalidQuantityError(Exception):
    """Raised when trying to sell or restock a negative quantity."""
    pass

class InvalidTransactionTypeError(Exception):
    """Raised when the transaction type is not 'sell' or 'restock'."""
    pass
