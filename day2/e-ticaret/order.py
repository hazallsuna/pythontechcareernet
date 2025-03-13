class Order:
    def __init__(self,customer,cart):
        self.customer = customer
        self.cart = cart
        self.total_amount = cart.get_total()
    
    def place_order(self):
        if self.total_amount > 0:
            print(f"\nOrder has been created successfully: ")
            print(self.customer)
            print("\nOrder details:")
            self.cart.display_cart()
            print(f"Total Amount : {self.total_amount} TL")
        else:
            print("\nBasket empty, your order could not be created!")