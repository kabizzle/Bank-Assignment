from account import Account

class SavingsAccount(Account):
    
    def transfer_to(self, account, sum):
        if account.get_customer() == self.get_customer() and self.get_balance() >= sum and self.get_balance() != 0:
            self.withdraw(sum)
            account.deposit(sum)
            return True
        return False