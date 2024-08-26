from order_dao import OrderDAO
from order import Order

class OrderService:
    def __init__(self, jdbc_url, jdbc_user, jdbc_password):
        self.order_dao = OrderDAO(jdbc_url, jdbc_user, jdbc_password)

    def place_order(self, customer_id, shipping_details, total_amount):
        try:
            order = Order(customer_id=customer_id, shipping_details=shipping_details, total_amount=total_amount)
            order_id = self.order_dao.place_order(order)
            return f"Order placed successfully. Order ID: {order_id}"
        except Exception as e:
            print(e)
            return "Error occurred while placing the order"

    def get_order(self, id):
        try:
            order = self.order_dao.get_order_by_id(id)
            if order:
                return order
            else:
                return "Order not found"
        except Exception as e:
            print(e)
            return "Error occurred while retrieving the order"
