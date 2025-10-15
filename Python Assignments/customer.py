class Customer:
    
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

def greet(customer):
    if customer.gender == 'Male':
        print(f"Hello Mr. {customer.name} sir")
    else:
        print(f"Hello Ms. {customer.name} ma'am")
cust = Customer("Ankit","Male")
greet(cust)