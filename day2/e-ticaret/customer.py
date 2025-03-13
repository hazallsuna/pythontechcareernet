class Customer:
    def __init__(self,name,email):
        self.name = name
        self.email = email
    
    def __str__(self):
        return f"Customer: {self.name}, E-mail: {self.email}"