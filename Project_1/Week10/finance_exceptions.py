"""Custom exceptions for the Finance project.

Every exception inherits from FinanceError, so code can catch one
specific problem (e.g. InsufficientFundsError) or any Finance rule
violation at once (FinanceError).

    FinanceError
    +-- InvalidAmountError
    +-- AccountNotFoundError
    +-- WithdrawalError
        +-- InsufficientFundsError
        +-- MinimumBalanceError
        +-- WithdrawalLimitError

Each exception keeps the values that explain the problem as attributes
(account number, balance, amount, limit) as well as in its message.
"""


class FinanceError(Exception):
    """Base class for every Finance rule violation."""


class InvalidAmountError(FinanceError):
    """A deposit or withdrawal amount is not a number greater than 0."""

    def __init__(self, account_number, amount, operation):
        self.account_number = account_number
        self.amount = amount
        self.operation = operation
        super().__init__(
            f'Account {account_number}: {amount!r} is not a valid '
            f'{operation} amount (must be a number greater than 0)')


class AccountNotFoundError(FinanceError):
    """A Client does not hold an Account with the requested number."""

    def __init__(self, client_no, account_number):
        self.client_no = client_no
        self.account_number = account_number
        super().__init__(
            f'Client {client_no} has no account numbered '
            f'{account_number!r}')


class WithdrawalError(FinanceError):
    """A withdrawal cannot be completed.

    Parent of the specific withdrawal problems, so they can be handled
    together. Records which account, its balance and the amount asked
    for; subclasses write the message explaining the rule broken.
    """

    def __init__(self, account_number, balance, amount, message):
        self.account_number = account_number
        self.balance = balance
        self.amount = amount
        super().__init__(f'Account {account_number}: {message}')


class InsufficientFundsError(WithdrawalError):
    """The withdrawal is larger than the account's balance."""

    def __init__(self, account_number, balance, amount):
        super().__init__(
            account_number, balance, amount,
            f'cannot withdraw ${amount}, balance is only ${balance}')


class MinimumBalanceError(WithdrawalError):
    """A Savings Account would fall below its minimum balance."""

    def __init__(self, account_number, balance, amount, minimum_balance):
        self.minimum_balance = minimum_balance
        super().__init__(
            account_number, balance, amount,
            f'withdrawing ${amount} from a balance of ${balance} would '
            f'leave ${balance - amount}, below the minimum balance of '
            f'${minimum_balance}')


class WithdrawalLimitError(WithdrawalError):
    """An Everyday Account withdrawal is above the per-withdrawal limit."""

    def __init__(self, account_number, balance, amount, limit):
        self.limit = limit
        super().__init__(
            account_number, balance, amount,
            f'withdrawal of ${amount} exceeds the maximum of ${limit} '
            f'per withdrawal')
