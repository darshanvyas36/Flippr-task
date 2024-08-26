import pymysql

class CartDAO:
    def __init__(self, jdbc_url, jdbc_user, jdbc_password):
        self.jdbc_url = jdbc_url
        self.jdbc_user = jdbc_user
        self.jdbc_password = jdbc_password

    def add_item(self, cart):
        conn = pymysql.connect(self.jdbc_url, self.jdbc_user, self.jdbc_password)
        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO cart (customer_id, product_id, quantity) VALUES (%s, %s, %s)"
                cursor.execute(sql, (cart.get_customer_id(), cart.get_product_id(), cart.get_quantity()))
                conn.commit()
        finally:
            conn.close()

    def update_item(self, cart):
        conn = pymysql.connect(self.jdbc_url, self.jdbc_user, self.jdbc_password)
        try:
            with conn.cursor() as cursor:
                sql = "UPDATE cart SET quantity = %s WHERE customer_id = %s AND product_id = %s"
                cursor.execute(sql, (cart.get_quantity(), cart.get_customer_id(), cart.get_product_id()))
                conn.commit()
        finally:
            conn.close()

    def remove_item(self, customer_id, product_id):
        conn = pymysql.connect(self.jdbc_url, self.jdbc_user, self.jdbc_password)
        try:
            with conn.cursor() as cursor:
                sql = "DELETE FROM cart WHERE customer_id = %s AND product_id = %s"
                cursor.execute(sql, (customer_id, product_id))
                conn.commit()
        finally:
            conn.close()

    def get_cart_by_customer_id(self, customer_id):
        conn = pymysql.connect(self.jdbc_url, self.jdbc_user, self.jdbc_password)
        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM cart WHERE customer_id = %s"
                cursor.execute(sql, (customer_id,))
                return cursor.fetchall()
        finally:
            conn.close()
