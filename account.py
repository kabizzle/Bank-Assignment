from customer import Customer


class Account:
    def __init__(self, customer):
        self.owner = customer
        self.balance = 0

    def get_customer(self):
        return self.owner

    def get_balance(self):
        return self.balance

    def deposit(self, sum):
        self.balance += sum

    def withdraw(self, sum):
        if self.get_balance() >= sum:
            self.balance -= sum
            return True
        else:
            return False

    def transfer_to(self, account, sum):
        return False
