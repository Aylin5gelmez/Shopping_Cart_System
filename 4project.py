class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def show_stock_status(self, stock):
        print("Stock status: {} items".format(stock))

class Cart:
    def __init__(self, products):
        self.products = []

    def add_product(self, product):
        if 0 < product.stock:
            self.products.append(product)
            product.stock -= 1
            print("{} has been added to your cart".format(product.name))
        else:
            print("{} could not be added due to insufficient stock".format(product.name))

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            product.stock += 1
            print("{} has been removed from your cart".format(product.name))
        else:
            print("{} is not in your cart".format(product.name))

    def total_amount(self):
        total = sum([product.price for product in self.products])
        return total

    def list_products(self):
        if not self.products:
            print("Your cart is empty")
        else:
            print("Products in your cart:")
            for product in self.products:
                print("{} - {} USD".format(product.name, product.price))

product1 = Product("Red Lentils", 25, 80)
product2 = Product("Rice", 15, 6)
product3 = Product("Pasta", 18, 3)

cart = Cart(product3)

cart.add_product(product1)
cart.add_product(product2)
cart.remove_product(product3)

cart.list_products()

print("Total Amount: {}".format(cart.total_amount()))

