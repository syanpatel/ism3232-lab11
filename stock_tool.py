# stock_tool.py
# Author: Syan Patel


class StockLookup:
    """A tool that knows about stock. It knows nothing about chatting."""

    def __init__(self, stock):
        """Store a dictionary that maps a product name to a count."""
        self.stock = stock

    def find_product(self, text):
        """Return the first known product named in text, or None."""
        for product in self.stock:
            if product in text.lower():
                return product
        return None

    def count_for(self, product):
        """Return the count for one product, or None if there is no such product."""
        if product in self.stock:
            return self.stock[product]
        return None
