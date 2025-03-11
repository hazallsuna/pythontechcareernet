from product import Product
from cart import Cart
from customer import Customer
from order import Order

def main():
    #kullanıcı bilgilerini aldık
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    customer = Customer(name, email)
    
    #sepeti oluştur
    cart = Cart()
    
    
    products = {
        "Laptop": Product(" HP 250 G10 Intel Core i5 Taşınabilir Bilgisayar", 15000, 5),
        "Phone": Product("Apple iPhone 13 128 GB Beyaz", 34000, 10),
        "Headphones": Product("JBL Tune 520BT Multi Connect Wireless Kulaklık", 1800, 15)
    }
    
    while True:
        #kullanıcıya işlem seçeneklerini göster
        print("\nSelect an operation:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Cart")
        print("4. Complete Order")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            #ürün ekleme 
            print("Available products:")
            for name, product in products.items():
                print(product)
            product_name = input("Enter product name: ")
            if product_name in products:
                quantity = int(input("Enter quantity: "))
                cart.add_product(products[product_name], quantity)
                print(f"{quantity} {product_name}(s) added to cart.")
            else:
                print("Invalid product name!")
        
        elif choice == "2":
            #ürün çıkarma
            product_name = input("Enter product name to remove: ")
            cart.remove_product(product_name)
            print(f"{product_name} removed from cart.")
        
        elif choice == "3":
            #sepeti görüntüleme
            print("\nCart Details:")
            cart.display_cart()
            print(f"Total: {cart.get_total()} TL")
        
        elif choice == "4":
            #siparişi tamamlama
            order = Order(customer, cart)
            order.place_order()
            break  #sipariş tamamlandığında döngüyü sonlandır
        
        elif choice == "5":
            #çıkış
            print("Exiting the program...")
            break
        
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()