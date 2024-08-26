import pymysql

class ProductDAO:
    def __init__(self, jdbc_url, jdbc_user, jdbc_password):
        self.jdbc_url = jdbc_url
        self.jdbc_user = jdbc_user
        self.jdbc_password = jdbc_password

    def add_product(self, product):
        conn = pymysql.connect(self.jdbc_url, self.jdbc_user, self.jdbc_password)
        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO products (name, description, price, category) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (product.get_name(), product.get_description(), product.get_price(), product.get_category()))
                conn.commit()
        finally:
            conn.close()

    def update_product(self, product):
        conn = pymysql.connect(self.jdbc_url, self.jdbc_user, self.jdbc_password)
        try:
            with conn.cursor() as cursor:
                sql = "UPDATE products SET name = %s, description = %s, price = %s, category = %s WHERE id = %s"
                cursor.execute(sql, (product.get_name(), product.get_description(), product.get_price(), product.get_category(), product.get_id()))
                conn.commit()
        finally:
            conn.close()

    def delete_product(self, product_id):
        conn = pymysql.connect(self.jdbc_url, self.jdbc_user, self.jdbc_password)
        try:
            with conn.cursor() as cursor:
                sql = "DELETE FROM products WHERE id = %s"
                cursor.execute(sql, (product_id,))
                conn.commit()
        finally:
            conn.close()

    def get_all_products(self):
        conn = pymysql.connect(self.jdbc_url, self.jdbc_user, self.jdbc_password)
        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM products"
                cursor.execute(sql)
                return cursor.fetchall()
        finally:
            conn.close()
