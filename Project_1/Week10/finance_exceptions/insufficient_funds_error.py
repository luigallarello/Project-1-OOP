from finance_exceptions.withdrawal_error import WithdrawalError


class InsufficientFundsError(WithdrawalError):
    """The withdrawal is larger than the account's balance."""

    def __init__(self, account_number, balance, amount):
        super().__init__(
            account_number, balance, amount,
            f'cannot withdraw ${amount}, balance is only ${balance}')
