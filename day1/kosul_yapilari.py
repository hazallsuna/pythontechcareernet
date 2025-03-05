a=10
b=4

print(f"Addition:{a+b}")
print(f"Subtraction:{a-b}")
print(f"Multiplication:{a*b}")
print(f"Division:{a/b}")
print(f"Floor Division:{a//b}")
print(f"Modules:{a%b}")
print(f"Exponentiation:{a**b}")

x=5
y=11

print(x>y)
print(x==y)
print(x != y)

print(x>3 and y<15) #true
print(x>3 or y<9) #true
print(not (x<6)) #false

age= 19

if age <18:
    print("You are not an adult!")
elif age == 18:
    print("You are just one the limit!")
else:
    print("You are adult.")
