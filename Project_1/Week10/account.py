from abc import ABC, abstractmethod

from finance_exceptions import InsufficientFundsError, InvalidAmountError
from transaction import Transaction


class Account(ABC):
    """Abstract base for every kind of bank account and its balance.

    Cannot be instantiated directly - each account type (SavingsAccount,
    EverydayAccount) must provide get_account_type() and its own
    withdrawal() rules. Shared state and validation live here.

    Keeps its transactions in a list in the order they happened.
    Responsible for validating and mutating
    its own balance through deposit() and withdrawal(), and for
    reporting its own state - it has no knowledge of which Client
    (if any) currently holds it.
    """

    def __init__(self, current_balance, account_number, account_holder_name):
        self.__current_balance = self.__validate_current_balance(
            current_balance)
        self.__account_number = self.__validate_account_number(
            account_number)
        self.account_holder_name = self.__validate_account_holder_name(
            account_holder_name)
        self.__transactions = []
        self.__next_transaction_id = 1

    @abstractmethod
    def get_account_type(self):
        """Return the account type name, e.g. 'Savings'."""

    def get_transactions(self):
        """Full history, oldest first, as a copy of the list."""
        return list(self.__transactions)

    def get_transaction_count(self, transaction_type=None):
        """Number of transactions, optionally of one type only."""
        if transaction_type is None:
            return len(self.__transactions)
        return len(self.get_transactions_by_type(transaction_type))

    def get_transactions_by_type(self, transaction_type):
        """History filtered to 'deposit' or 'withdrawal', in order."""
        if transaction_type not in ('deposit', 'withdrawal'):
            print(f'Rejected: {transaction_type!r} is not a valid '
                  f'transaction type')
            return []
        return [txn for txn in self.__transactions
                if txn.get_transaction_type() == transaction_type]

    def get_transactions_above(self, amount):
        """History entries larger than amount, in order."""
        if (not isinstance(amount, (int, float))
                or isinstance(amount, bool)):
            print(f'Rejected: {amount!r} is not a valid amount')
            return []
        return [txn for txn in self.__transactions
                if txn.get_transaction_amt() > amount]

    def __validate_current_balance(self, current_balance):
        if (isinstance(current_balance, (int, float))
                and not isinstance(current_balance, bool)
                and current_balance >= 0):
            return current_balance
        print(f'Invalid current balance {current_balance!r} - '
              f'defaulting to 0')
        return 0

    def __validate_account_number(self, account_number):
        if (isinstance(account_number, int)
                and not isinstance(account_number, bool)
                and account_number >= 0):
            return account_number
        print(f'Invalid account number {account_number!r} - '
              f'defaulting to 0')
        return 0

    def __validate_account_holder_name(self, account_holder_name):
        if (isinstance(account_holder_name, str)
                and account_holder_name.strip() != ''):
            return account_holder_name
        print(f'Invalid account holder name {account_holder_name!r} - '
              f'defaulting to "Unknown"')
        return 'Unknown'

    def get_current_balance(self):
        return self.__current_balance

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        if (isinstance(account_number, int)
                and not isinstance(account_number, bool)
                and account_number >= 0):
            self.__account_number = account_number
        else:
            print(f'Rejected: {account_number!r} is not a valid '
                  f'account number')

    def set_account_holder_name(self, account_holder_name):
        if (isinstance(account_holder_name, str)
                and account_holder_name.strip() != ''):
            self.account_holder_name = account_holder_name
        else:
            print(f'Rejected: {account_holder_name!r} is not a valid '
                  f'account holder name')

    def __str__(self):
        return (f'Current Balance: {self.get_current_balance()}\n'
                f' Account Number: {self.get_account_number()}\n'
                f' Type: {self.get_account_type()}\n'
                f' Account Name: {self.account_holder_name}')

    def __repr__(self):
        return (f'Account(current balance={self.get_current_balance()!r}, '
                f'account number={self.get_account_number()!r}, '
                f'type={self.get_account_type()!r}, '
                f'account holder name={self.account_holder_name!r})')

    def _validate_amount(self, amount, label):
        """Raise InvalidAmountError unless amount is a number above 0.

        Single underscore so subclasses can check an amount before
        applying their own withdrawal rule.
        """
        if (isinstance(amount, (int, float))
                and not isinstance(amount, bool) and amount > 0):
            return
        raise InvalidAmountError(self.get_account_number(), amount, label)

    def __record_transaction(self, transaction_type, amount, desc):
        txn = Transaction(self.__next_transaction_id, transaction_type,
                          amount, desc, status='Processed')
        self.__transactions.append(txn)
        self.__next_transaction_id += 1

    def deposit(self, deposit_amt):
        """Add funds; raises InvalidAmountError before changing anything."""
        self._validate_amount(deposit_amt, 'deposit')
        self.__current_balance += deposit_amt
        self.__record_transaction('deposit', deposit_amt, 'Deposit')
        print(f'Your new balance is ${self.__current_balance}.')

    @abstractmethod
    def withdrawal(self, withdrawal_amt):
        """Withdraw funds under this account type's own rules.

        Subclasses apply their rule, then call super().withdrawal() to
        reuse the shared validation and balance update below. Raises
        InvalidAmountError or InsufficientFundsError before any change
        is made to the balance or the transaction history.
        """
        self._validate_amount(withdrawal_amt, 'withdrawal')
        if withdrawal_amt > self.__current_balance:
            raise InsufficientFundsError(self.get_account_number(),
                                         self.__current_balance,
                                         withdrawal_amt)
        self.__current_balance -= withdrawal_amt
        self.__record_transaction('withdrawal', withdrawal_amt, 'Withdrawal')
        print(f'Your new balance is ${self.__current_balance}.')

    def display_current_balance(self):
        print(f'Your current Balance is ${self.__current_balance}.')
