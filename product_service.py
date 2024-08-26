from product_dao import ProductDAO
from product import Product

class ProductService:
    def __init__(self, jdbc_url, jdbc_user, jdbc_password):
        self.product_dao = ProductDAO(jdbc_url, jdbc_user, jdbc_password)

    def add_product(self, name, description, price, category):
        try:
            product = Product(name=name, description=description, price=price, category=category)
            self.product_dao.add_product(product)
            return f"Product added successfully. Product ID: {product.get_id()}"
        except Exception as e:
            print(e)
            return "Error occurred while adding the product"

    def update_product(self, id, name, description, price, category):
        try:
            product = Product(id=id, name=name, description=description, price=price, category=category)
            self.product_dao.update_product(product)
            return "Product updated successfully"
        except Exception as e:
            print(e)
            return "Error occurred while updating the product"

    def delete_product(self, id):
        try:
            self.product_dao.delete_product(id)
            return "Product deleted successfully"
        except Exception as e:
            print(e)
            return "Error occurred while deleting the product"

    def get_all_products(self):
        try:
            return self.product_dao.get_all_products()
        except Exception as e:
            print(e)
            return None
