from finance_exceptions.finance_error import FinanceError


class InvalidAmountError(FinanceError):
    """A deposit or withdrawal amount is not a number greater than 0."""

    def __init__(self, account_number, amount, operation):
        self.account_number = account_number
        self.amount = amount
        self.operation = operation
        super().__init__(
            f'Account {account_number}: {amount!r} is not a valid '
            f'{operation} amount (must be a number greater than 0)')
