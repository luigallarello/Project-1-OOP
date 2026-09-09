from account import Account

class SavingsAccount(Account):
        def __init__(self, current_balance, account_number, account_holder_name, interest_rate, min_balance=0):
            super().__init__(current_balance, account_number, account_holder_name)
            self.__interest_rate = self.set_interest_rate(interest_rate)
            self.__min_balance = min_balance

        def get_account_type(self):
            return 'Savings'

        def get_interest_rate(self):
            return self.__interest_rate

        def set_interest_rate(self, interest_rate):
            if isinstance(interest_rate, float):
                interest_rate = self.__interest_rate
                return self.__interest_rate
            else:
                print(f'Not a valid interest rate')
                return False

        def _withdrawal(self, withdrawal_amt):
            if self.current_balance > self.__min_balance:
                withdrawal_process = super()._withdrawal()
            else:
                print('Not enough funds available to withdraw')