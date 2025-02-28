from cart import Cart
from product import Product
from product_manager import ProductManager

manager = ProductManager()

product1 = Product("Laptop", 800, 5)
product2 = Product("Phone", 500, 10)

manager.add_product(product1)
manager.add_product(product2)

cart = Cart()
cart.add_to_cart(product1)
cart.add_to_cart(product2)

cart.display_cart()
print(f"Total cart value: {cart.total_cart_value()}")
