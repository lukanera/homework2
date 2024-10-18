from datetime import datetime

class Customer:
    def __init__(self, name, date_of_birth, balance, age = None):
        self.name = name
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
        self.balance = balance
        self.age = age
    
    def deposit(self, money):
        self.balance += money
        return self.balance

    def withdraw(self, money):
        if money <= self.balance:
            self.balance -= money
        else:
            print("ERROR, you broke!")
        return self.balance

    @property
    def age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        return age

    @age.setter
    def age(self, new_age):
        age = self.age + new_age


class Bank:
    def __init__(self, name, base_budget):
        self.name = name
        self.base_budget = base_budget
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)
        return self.customers

    def remove_customer(self, customer):
        self.customers.remove(customer)
        return self.customers
   
    def can_get_loan(self, customer_name, loan):
        for customer in self.customers:
            if customer.name == customer_name:
                if loan * 0.5 <= customer.balance:
                    return True 
                else:
                    return False    
        
        print(f"Customer {customer_name} not found!")
        return False   


    @property
    def budget(self):
        total_balance = sum(customer.balance for customer in self.customers)
        return self.base_budget + total_balance

    @budget.setter
    def budget(self, new_budget):
        self.base_budget = new_budget

    def show(self):
        return self.budget


my_bank = Bank("bank", 1100)

customer1 = Customer("jemaliko", "2001-11-09", 100, 23)
my_bank.add_customer(customer1)

print(customer1.age)