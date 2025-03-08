class BankAccount:
    def __init__(self,balance):
        self.__balance=balance #bakiye bilgisi gizli

    def show_balance(self):
        print(f"Bakiye: {self.__balance} USD")

#banka hesabı nesnesi oluşturuluyor
account=BankAccount(8000) 

#bakiye ekrana yazdır
account.show_balance()