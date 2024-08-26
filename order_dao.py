import pymysql

class OrderDAO:
    def __init__(self, jdbc_url, jdbc_user, jdbc_password):
        self.jdbc_url = jdbc_url
        self.jdbc_user = jdbc_user
        self.jdbc_password = jdbc_password

    def place_order(self, order):
        conn = pymysql.connect(self.jdbc_url, self.jdbc_user, self.jdbc_password)
        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO orders (customer_id, shipping_details, total_amount) VALUES (%s, %s, %s)"
                cursor.execute(sql, (order.get_customer_id(), order.get_shipping_details(), order.get_total_amount()))
                conn.commit()
                return cursor.lastrowid
        finally:
            conn.close()

    def get_order_by_id(self, order_id):
        conn = pymysql.connect(self.jdbc_url, self.jdbc_user, self.jdbc_password)
        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM orders WHERE id = %s"
                cursor.execute(sql, (order_id,))
                result = cursor.fetchone()
                if result:
                    return Order(id=result[0], customer_id=result[1], shipping_details=result[2], total_amount=result[3])
        finally:
            conn.close()
        return None
