from cart_dao import CartDAO
from cart import Cart

class CartService:
    def __init__(self, jdbc_url, jdbc_user, jdbc_password):
        self.cart_dao = CartDAO(jdbc_url, jdbc_user, jdbc_password)

    def add_item_to_cart(self, customer_id, product_id, quantity):
        try:
            cart = Cart(customer_id=customer_id, product_id=product_id, quantity=quantity)
            self.cart_dao.add_item(cart)
            return "Item added to cart successfully"
        except Exception as e:
            print(e)
            return "Error occurred while adding item to cart"

    def update_cart_item(self, customer_id, product_id, quantity):
        try:
            cart = Cart(customer_id=customer_id, product_id=product_id, quantity=quantity)
            self.cart_dao.update_item(cart)
            return "Cart item updated successfully"
        except Exception as e:
            print(e)
            return "Error occurred while updating cart item"

    def remove_item_from_cart(self, customer_id, product_id):
        try:
            self.cart_dao.remove_item(customer_id, product_id)
            return "Item removed from cart successfully"
        except Exception as e:
            print(e)
            return "Error occurred while removing item from cart"

    def get_cart(self, customer_id):
        try:
            return self.cart_dao.get_cart_by_customer_id(customer_id)
        except Exception as e:
            print(e)
            return None
