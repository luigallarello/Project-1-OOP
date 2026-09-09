from account import Account

class SavingsAccount(Account):
        def __init__(self, current_balance, account_number, account_holder_name, interest_rate, min_balance=0):
            super().__init__(current_balance, account_number)
            self.set_interest_rate(interest_rate)
            self.__min_balance = min_balance
            

        def get_account_type(self):
            return 'Savings'

        def get_interest_rate(self):
            return self.__interest_rate

        def set_interest_rate(self, interest_rate):
            if isinstance(interest_rate, (int, float)) and not isinstance(interest_rate, bool) and interest_rate >= 0:
                self.__interest_rate = float(interest_rate)
                return True
            else:
                print('Not a valid interest rate')
                return False

        def _withdrawal(self, withdrawal_amt):
            if self.current_balance > self.__min_balance:
                super()._withdrawal(withdrawal_amt)
            else:
                print('Not enough funds available to withdraw')