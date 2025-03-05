import getpass

name = input("Enter your name:")
print(f"Hi,{name}!")

age=int(input ("Enter your age:"))

print(f"Next year,you will be {age +1} years old.")

name,age = input("Enter your name and age(seperated by space):").split()
age=int(age)

print("Your Name:",name)
print("Your Age:",age)

try: 
    age = int(input("Enter your age:"))
    print("Your age is",age)
except ValueError:
    print("Invalid input! Please enter an integer.")

password= getpass.getpass("Enter your password:")
print("Your password has been successfully recorded.")