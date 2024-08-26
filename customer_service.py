from customer_dao import CustomerDAO
from customer import Customer
import bcrypt

class CustomerService:
    def __init__(self, jdbc_url, jdbc_user, jdbc_password):
        self.customer_dao = CustomerDAO(jdbc_url, jdbc_user, jdbc_password)

    def sign_up(self, name, email, password, address):
        try:
            if self.customer_dao.email_exists(email):
                return "Email already registered"

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            customer = Customer(name=name, email=email, password_hash=hashed_password.decode('utf-8'), address=address)
            self.customer_dao.add_customer(customer)
            return f"Sign up successful. Customer ID: {customer.get_id()}"
        except Exception as e:
            print(e)
            return "Error occurred during sign up"

    def sign_in(self, email, password):
        try:
            customer = self.customer_dao.get_customer_by_email(email)
            if customer and bcrypt.checkpw(password.encode('utf-8'), customer.get_password_hash().encode('utf-8')):
                return "Sign in successful. Token: [JWT Token]"
            else:
                return "Invalid email or password"
        except Exception as e:
            print(e)
            return "Error occurred during sign in"
