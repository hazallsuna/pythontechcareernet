class Vehicle:
    def move(self):
        print("Araba çalışıyor..")

#araba sınıfı,vehicle sınıfından miras alır
class Car(Vehicle): 
    def __init__(self,brand):
        self.brand = brand #arabayı tanımlayan kurucu metot

car = Car("Tesla")

car.move()
