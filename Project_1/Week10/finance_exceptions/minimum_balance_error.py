from finance_exceptions.withdrawal_error import WithdrawalError


class MinimumBalanceError(WithdrawalError):
    """A Savings Account would fall below its minimum balance."""

    def __init__(self, account_number, balance, amount, minimum_balance):
        self.minimum_balance = minimum_balance
        super().__init__(
            account_number, balance, amount,
            f'withdrawing ${amount} from a balance of ${balance} would '
            f'leave ${balance - amount}, below the minimum balance of '
            f'${minimum_balance}')
