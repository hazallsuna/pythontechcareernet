import getpass

print("User Registration Screen")

name= input("Enter your name:")

while True:
    try:
        age = int(input("Enter your age:"))
        if age <18:
            print("Users under 18 cannot register")
            exit()
        break
    except ValueError:
        print("Invalid input! Please enter only numbers")

if age < 25:
    category="Student"
    discount=50
elif age >= 65:
    category="Aged"
    discount=30
else:
    category="Adult"
    discount=0

print(f"You are categorized as:{category}")
print(f"Your bus card discount rate is:{discount}%")

while True:
    password= getpass.getpass("Create your password:")
    confirm_password=getpass.getpass("Re-enter your password:")

    if password == confirm_password:
        print("Password successfully created")
        break
    else:
        print("Passwords do not match! Please try again")

print("USER LOGIN")
attempts=3
while attempts >0:
    entered_password=getpass.getpass("Enter your password:")
    
    if entered_password==password:
        print(f"Welcome,{name}!")
        break
    else:
        attempts -=1
        print(f"Incorrect password! Attempts left:{attempts}")
        if attempts == 0:
            print("You have entered wrong password 3 times! Your account is locked")
            exit()

balance = float(input("Enter your bus card balance ($):"))
ticket_price= 2.50

if balance > 0:
        final_price = ticket_price*(1-discount/100)
        print(f"Ticket Price after discount: ${final_price:.2f}")

        if balance >= final_price:
            balance -= final_price
            print(f"Ticket used! Remaining balance: ${balance: .2f}")
        else:
            print("Please reload your card")

elif balance == 0:
         print("Your balance is empty! Please reload your card")
else:
         print("Invalid balance amount.")
