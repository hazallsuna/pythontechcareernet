"""
34,4list_example= [1,2,3]
print(list_example[4]) #IndexError
print(list_example[-4]) #IndexError
"""

try:
    x= int(input("Enter a number:"))
    print(f"You entered:{x}")
except ValueError: #int verdik ama mesela float girildiğinde yani değer uyuşmazlığı
    print("Error: Please enter valid number!")

print("Hello again")

try:
    file = open("day2/example.txt","r") #çalışır
    file = open("example.txt","r") #hata alır
    content =file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found!")
finally: #ne olursa olsun try başarılı olsa da hata olsa da finally her zaman çalışır
    file.close()
    print("File closed") 

class NegativeNumberError(Exception):
    pass

def square_root(number):
    if number <0:
        raise NegativeNumberError("Error: Cannot calculate square root of a negative number!")
    return number**0.5
print(square_root(81))

try:
    n=0
    res=100/n
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Enter valid number!")
else:
    print("Result:",res)
finally:
    print("Complete")

def divide(a, b):
    """Function that raises an exception for division by zero."""
    if b == 0:
        raise ZeroDivisionError("Error: Cannot divide by zero!")  # raise manuel hata fırlatma sağlıyor
    return a / b

print(divide(10, 2))  #çalışır
print(divide(10, 0))  #ZeroDivisionError hatası 