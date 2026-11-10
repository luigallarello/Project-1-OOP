from finance_exceptions.finance_error import FinanceError


class AccountNotFoundError(FinanceError):
    """A Client does not hold an Account with the requested number."""

    def __init__(self, client_no, account_number):
        self.client_no = client_no
        self.account_number = account_number
        super().__init__(
            f'Client {client_no} has no account numbered '
            f'{account_number!r}')
