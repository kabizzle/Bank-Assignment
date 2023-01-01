from customer import Customer
from account import Account
from personal_account import PersonalAccount
from savings_account import SavingsAccount

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.accounts = []

    def get_name(self):
        return self.name

    def get_customers(self):
        return self.customers

    def get_customers_by_name(self, name):
        customer_list = []
        for i in self.get_customers():
            if i.get_name() == name:
                customer_list.append(i)
        return customer_list

    def get_customer_by_id(self, id):
        for i in self.get_customers():
            if i.get_id() == id:
                return i
        return None

    # def add_account(self, customer):
    #     if customer in self.get_customers():
    #         customer_account = Account(customer)
    #         self.accounts.append(customer_account)
    #         return customer_account
    #     else:
    #         return
    
    def add_savings_account(self, customer):
        if customer in self.get_customers():
            customer_account = SavingsAccount(customer)
            self.accounts.append(customer_account)
            return customer_account
        else:
            return
    
    def add_personal_account(self, customer):
        if customer in self.get_customers():
            customer_account = PersonalAccount(customer)
            self.accounts.append(customer_account)
            return customer_account
        else:
            return

    def add_customer(self, customer):
        if customer not in self.get_customers():
            self.customers.append(customer)

    def remove_customer(self, customer):
        if customer in self.get_customers():
            self.customers.remove(customer)

    def get_accounts(self, customer):
        account_list = []
        for i in self.accounts:
            if i.get_customer() == customer:
                account_list.append(i)
        return account_list
