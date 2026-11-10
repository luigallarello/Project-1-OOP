from finance_exceptions.finance_error import FinanceError


class WithdrawalError(FinanceError):
    """A withdrawal cannot be completed.

    Parent of the specific withdrawal problems so they can be handled
    together. Records which account, its balance and the amount asked
    for; each subclass writes the message explaining the rule broken.
    """

    def __init__(self, account_number, balance, amount, message):
        self.account_number = account_number
        self.balance = balance
        self.amount = amount
        super().__init__(f'Account {account_number}: {message}')
