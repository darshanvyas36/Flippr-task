class Cart:
    def __init__(self, customer_id=None, product_id=None, quantity=None):
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity

    # Getters and Setters
    def get_customer_id(self):
        return self.customer_id

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_product_id(self):
        return self.product_id

    def set_product_id(self, product_id):
        self.product_id = product_id

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"Cart(customer_id={self.customer_id}, product_id={self.product_id}, quantity={self.quantity})"
