from account import Account

class SavingsAccount(Account):
        MINIMUM_BALANCE = 100

        def __init__(self, current_balance, account_number, account_holder_name, interest_rate):
            super().__init__(current_balance, account_number, account_holder_name)
            self.set_interest_rate(interest_rate)

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

        def withdrawal(self, withdrawal_amt):
            if self.get_current_balance() - withdrawal_amt >= self.MINIMUM_BALANCE:
                super().withdrawal(withdrawal_amt)
            else:
                print(f'Rejected: withdrawal would drop balance below the '
                      f'minimum balance of ${self.MINIMUM_BALANCE}.')
