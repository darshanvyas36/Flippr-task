class Product:
    def __init__(self, id=None, name=None, description=None, price=None, category=None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    # Getters and Setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_category(self):
        return self.category

    def set_category(self, category):
        self.category = category

    def __str__(self):
        return f"Product(id={self.id}, name={self.name}, description={self.description}, price={self.price}, category={self.category})"
