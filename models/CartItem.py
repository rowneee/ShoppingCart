class CartItem:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price and self.quantity == other.quantity

    def json(self):
        return {'name': self.name, 'price': self.price, 'quantity': self.quantity}
