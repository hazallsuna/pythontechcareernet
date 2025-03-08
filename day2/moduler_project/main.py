from math_operations import addition,subtraction
import user_management as um

print("Moduler Project Example")

name = input("Please enter name:")
age = int(input("Please enter age:"))

print(um.user_register(name,age))

password = input ("Create your password:")
entered_password = input ("Enter your password for login:")
print(um.user_login(name,password,entered_password))


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", addition(num1, num2))
print("Subtraction:", subtraction(num1, num2))