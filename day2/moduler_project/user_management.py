def user_register(name,age):
    if age <18:
        return "Sorry, don't register under the age of 18"
    return print(f"User {name} successfully saved!")

def user_login(name,password,registered_password):
    if password == registered_password:
        return print(f"Welcome , {name}")
    return "Wrong password!"