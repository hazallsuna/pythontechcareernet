class Car:
    def __init__(self,brand,model,year):
        self.brand=brand #marka 
        self.model=model #model
        self.year=year #yıl

    def start_engine(self):
        print(f"{self.brand} şuan çalışıyor..")

#araba nesnesi oluşturuluyor
car= Car("BMW","X5",2023)

print(car.brand) #markayı ekrana yazdır
car.start_engine() #methodu çalıştır