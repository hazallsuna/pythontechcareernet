def addition (a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b==0:
        raise ZeroDivisionError("Error: Cannot divide by zero!")  # raise manuel hata fırlatma sağlıyor
    return a/b 