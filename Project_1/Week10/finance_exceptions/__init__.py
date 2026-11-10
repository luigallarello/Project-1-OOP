"""Custom exceptions for the Finance project, one class per module.

    FinanceError
    +-- InvalidAmountError
    +-- AccountNotFoundError
    +-- TransactionStatusError
    +-- WithdrawalError
        +-- InsufficientFundsError
        +-- MinimumBalanceError
        +-- WithdrawalLimitError

Each exception keeps the values that explain the problem (account number,
balance, amount, limit) as attributes as well as in its message.
"""
from finance_exceptions.account_not_found_error import AccountNotFoundError
from finance_exceptions.finance_error import FinanceError
from finance_exceptions.insufficient_funds_error import InsufficientFundsError
from finance_exceptions.invalid_amount_error import InvalidAmountError
from finance_exceptions.minimum_balance_error import MinimumBalanceError
from finance_exceptions.transaction_status_error import (
    TransactionStatusError)
from finance_exceptions.withdrawal_error import WithdrawalError
from finance_exceptions.withdrawal_limit_error import WithdrawalLimitError

__all__ = [
    'AccountNotFoundError', 'FinanceError', 'InsufficientFundsError',
    'InvalidAmountError', 'MinimumBalanceError', 'TransactionStatusError',
    'WithdrawalError', 'WithdrawalLimitError',
]
