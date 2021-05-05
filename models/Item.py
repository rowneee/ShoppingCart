class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def json(self):
        return {'name': self.name, 'price': self.price, 'quantity': self.quantity}

