from product import Product
from product_manager import ProductManager

# Kreiramo instancu ProductManager
manager = ProductManager()

# Dodajemo proizvode
product1 = Product("Laptop", 800, 5)
product2 = Product("Phone", 500, 10)

manager.add_product(product1)
manager.add_product(product2)

# Prikaz proizvoda
manager.display_products()

# Prikaz ukupne vrednosti inventara
print(f"Total inventory value: {manager.total_inventory_value()}")
