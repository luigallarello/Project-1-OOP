from account import Account
from finance_exceptions import WithdrawalLimitError


class EverydayAccount(Account):
    """An Account with a maximum amount per single withdrawal."""

    MAX_WITHDRAWAL = 1000

    def __init__(self, current_balance, account_number, account_holder_name):
        super().__init__(current_balance, account_number,
                         account_holder_name)

    def get_account_type(self):
        return 'Everyday'

    def withdrawal(self, withdrawal_amt):
        """Withdraw funds, up to MAX_WITHDRAWAL in a single withdrawal.

        Raises WithdrawalLimitError (or the errors from Account) before
        the balance or transaction history is changed.
        """
        self._check_amount(withdrawal_amt, 'withdrawal')
        # Check the rule before calling super() so nothing changes on failure.
        if withdrawal_amt > self.MAX_WITHDRAWAL:
            raise WithdrawalLimitError(self.get_account_number(),
                                       self.get_current_balance(),
                                       withdrawal_amt, self.MAX_WITHDRAWAL)
        super().withdrawal(withdrawal_amt)
