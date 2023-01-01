from account import Account

class PersonalAccount(Account):

    def transfer_to(self, account, sum):
        if self.get_balance() >= sum and self.get_balance() != 0:
                self.withdraw(sum)
                account.deposit(sum)
                return True
        return False
