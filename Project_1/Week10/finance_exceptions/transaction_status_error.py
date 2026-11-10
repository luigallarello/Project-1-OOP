from finance_exceptions.finance_error import FinanceError


class TransactionStatusError(FinanceError):
    """A Transaction is not Pending, so it cannot be processed."""

    def __init__(self, transaction_id, status):
        self.transaction_id = transaction_id
        self.status = status
        super().__init__(
            f'Transaction {transaction_id} is {status}, only a Pending '
            f'transaction can be processed')
