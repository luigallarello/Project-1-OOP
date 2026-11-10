from finance_exceptions.withdrawal_error import WithdrawalError


class WithdrawalLimitError(WithdrawalError):
    """An Everyday Account withdrawal is above the per-withdrawal limit."""

    def __init__(self, account_number, balance, amount, limit):
        self.limit = limit
        super().__init__(
            account_number, balance, amount,
            f'withdrawal of ${amount} exceeds the maximum of ${limit} '
            f'per withdrawal')
