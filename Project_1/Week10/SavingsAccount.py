from account import Account
from finance_exceptions import MinimumBalanceError


class SavingsAccount(Account):
    """An Account that must always keep a minimum balance."""

    MINIMUM_BALANCE = 100

    def __init__(self, current_balance, account_number, account_holder_name,
                 interest_rate):
        super().__init__(current_balance, account_number,
                         account_holder_name)
        self.set_interest_rate(interest_rate)

    def get_account_type(self):
        return 'Savings'

    def get_interest_rate(self):
        return self.__interest_rate

    def set_interest_rate(self, interest_rate):
        if (isinstance(interest_rate, (int, float))
                and not isinstance(interest_rate, bool)
                and interest_rate >= 0):
            self.__interest_rate = float(interest_rate)
            return True
        print('Not a valid interest rate')
        return False

    def withdrawal(self, withdrawal_amt):
        """Withdraw funds, keeping at least MINIMUM_BALANCE in the account.

        Raises MinimumBalanceError (or the errors from Account) before
        the balance or transaction history is changed.
        """
        self._validate_amount(withdrawal_amt, 'withdrawal')
        balance = self.get_current_balance()
        if balance - withdrawal_amt < self.MINIMUM_BALANCE:
            raise MinimumBalanceError(self.get_account_number(), balance,
                                      withdrawal_amt, self.MINIMUM_BALANCE)
        super().withdrawal(withdrawal_amt)
