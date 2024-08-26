class Order:
    def __init__(self, id=None, customer_id=None, shipping_details=None, total_amount=None):
        self.id = id
        self.customer_id = customer_id
        self.shipping_details = shipping_details
        self.total_amount = total_amount

    # Getters and Setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_customer_id(self):
        return self.customer_id

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_shipping_details(self):
        return self.shipping_details

    def set_shipping_details(self, shipping_details):
        self.shipping_details = shipping_details

    def get_total_amount(self):
        return self.total_amount

    def set_total_amount(self, total_amount):
        self.total_amount = total_amount

    def __str__(self):
        return f"Order(id={self.id}, customer_id={self.customer_id}, shipping_details={self.shipping_details}, total_amount={self.total_amount})"
