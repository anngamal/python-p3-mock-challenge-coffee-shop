
class Order:

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

@property
def price(self):
    return self._price

@price.setter
def price(self, new_price):
    if 1 <= new_price >=10:
        self._price = new_price
    else:
        raise ValueError(f"Not accepted price")