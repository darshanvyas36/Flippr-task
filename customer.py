class Customer:
    def __init__(self, id=None, name=None, email=None, password_hash=None, address=None):
        self.id = id
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.address = address

    # Getters and Setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_password_hash(self):
        return self.password_hash

    def set_password_hash(self, password_hash):
        self.password_hash = password_hash

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def __str__(self):
        return f"Customer(id={self.id}, name={self.name}, email={self.email}, address={self.address})"
