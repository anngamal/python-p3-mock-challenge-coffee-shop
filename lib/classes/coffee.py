class Coffee:
    def __init__(self, name):
        self.name = name
        self.orders = []
    
    def get_customers(self):
        # customers = []
        # for order in self.orders:
        #     customers.append(order.customer)
        # return customers
        return [order.customer for order in self.orders]


        
    
    def num_orders(self, customer):
        return self.get_customers().count(customer)
    
    def average_price(self, customer):
        return sum([r.price for r in self.orders if r.customer == customer]) / len(self.orders)