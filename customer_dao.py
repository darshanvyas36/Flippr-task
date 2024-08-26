import pymysql

class CustomerDAO:
    def __init__(self, jdbc_url, jdbc_user, jdbc_password):
        self.jdbc_url = jdbc_url
        self.jdbc_user = jdbc_user
        self.jdbc_password = jdbc_password

    def email_exists(self, email):
        conn = pymysql.connect(self.jdbc_url, self.jdbc_user, self.jdbc_password)
        try:
            with conn.cursor() as cursor:
                sql = "SELECT COUNT(*) FROM customers WHERE email = %s"
                cursor.execute(sql, (email,))
                result = cursor.fetchone()
                return result[0] > 0
        finally:
            conn.close()

    def add_customer(self, customer):
        conn = pymysql.connect(self.jdbc_url, self.jdbc_user, self.jdbc_password)
        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO customers (name, email, password_hash, address) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (customer.get_name(), customer.get_email(), customer.get_password_hash(), customer.get_address()))
                conn.commit()
        finally:
            conn.close()

    def get_customer_by_email(self, email):
        conn = pymysql.connect(self.jdbc_url, self.jdbc_user, self.jdbc_password)
        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM customers WHERE email = %s"
                cursor.execute(sql, (email,))
                result = cursor.fetchone()
                if result:
                    customer = Customer(id=result[0], name=result[1], email=result[2], password_hash=result[3], address=result[4])
                    return customer
        finally:
            conn.close()
        return None
