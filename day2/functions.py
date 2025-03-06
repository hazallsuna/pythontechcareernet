"""
print("Hi, Hazal")
print("Hi, Ayşe")
print("Hi, Sena")
bu şekilde yazmaktansa fonksiyon ile aşağıdaki gibi yazıyoruz
"""
def greet(name):
    print(f"Hi",{name})

greet("Hazal")

def add(a,b):
    return a+b
print("Result:",add(14,5))

def welcome(name="Guest"):
    print(f"Welcome,{name}")

welcome() #parametresiz çağırdık default değer verecek guest oluyor o da

def operations(number):
    square = number ** 2
    cube = number ** 3
    return square, cube

sq,cb = operations(5)
print("square:", sq)
print("cube:", cb)

def cube(x):
    return x**3

print(cube(4)) #4ü parametre olarak verdik ve küpünü aldı

cube_lambda = lambda x: x**3 #anonim fonksiyon
print(cube_lambda(3))

def is_even(number): #cift mi tek mi bakıyoruz
    return number %2==0

def check_number(number):
    if is_even(number):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd")

check_number(12)
check_number(9)
check_number(13)

def substract( a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "Error: Division zero" #payda sıfır olamaz    
    return a/b

num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
#ondalıklı sayı girişi olabilir

print("Select operations: +,-,*,/")
operation= input("Operation:")

if operation == "+":
    print("Result:",add(num1,num2))
elif operation == "-":
    print("Result:",substract(num1,num2))
elif operation == "*":
    print("Result:",multiply(num1,num2))
elif operation == "/":
    print("Result:",divide(num1,num2))
else:
    print("Invalid operation!")

