from finance_exceptions import FinanceError, TransactionStatusError
from validation import is_number, is_whole_number


class Transaction:
    """A single deposit or withdrawal request and its status.

    A Transaction does not keep a permanent reference to an Account -
    process_transaction() receives one temporarily to apply the
    transaction, then lets it go. Its responsibility is the
    transaction's own data and its Pending/Processed/Cancelled
    status.

    An invalid amount falls back to 0. Such a transaction can be created
    but never processed, because an Account refuses an amount of 0.
    """

    TRANSACTION_TYPES = ('deposit', 'withdrawal')
    STATUSES = ('Pending', 'Processed', 'Cancelled')

    def __init__(self, transaction_id, transaction_type, transaction_amt,
                 transaction_desc, status='Pending'):
        self.__transaction_id = self.__validate_transaction_id(
            transaction_id)
        self.__transaction_type = self.__validate_transaction_type(
            transaction_type)
        self.__transaction_amt = self.__validate_transaction_amt(
            transaction_amt)
        self.__transaction_desc = self.__validate_transaction_desc(
            transaction_desc)
        self.__status = self.__validate_status(status)

    def __validate_transaction_id(self, transaction_id):
        if is_whole_number(transaction_id):
            return transaction_id
        print(f'Invalid transaction ID {transaction_id!r} - '
              f'defaulting to 0')
        return 0

    def __validate_transaction_type(self, transaction_type):
        if transaction_type in self.TRANSACTION_TYPES:
            return transaction_type
        print(f'Invalid transaction type {transaction_type!r} - '
              f'defaulting to "deposit"')
        return 'deposit'

    def __validate_transaction_amt(self, transaction_amt):
        if is_number(transaction_amt):
            return transaction_amt
        print(f'Invalid transaction amount {transaction_amt!r} - '
              f'defaulting to 0')
        return 0

    def __validate_transaction_desc(self, transaction_desc):
        if isinstance(transaction_desc, str):
            return transaction_desc
        print(f'Invalid transaction description {transaction_desc!r} - '
              f'defaulting to ""')
        return ''

    def __validate_status(self, status):
        if status in self.STATUSES:
            return status
        print(f'Invalid status {status!r} - defaulting to "Pending"')
        return 'Pending'

    def get_transaction_id(self):
        return self.__transaction_id

    def get_transaction_type(self):
        return self.__transaction_type

    def get_transaction_amt(self):
        return self.__transaction_amt

    def get_status(self):
        return self.__status

    @property
    def transaction_desc(self):
        return self.__transaction_desc

    @transaction_desc.setter
    def transaction_desc(self, transaction_desc):
        self.set_transaction_desc(transaction_desc)

    def set_transaction_id(self, transaction_id):
        if is_whole_number(transaction_id):
            self.__transaction_id = transaction_id
        else:
            print(f'Rejected: {transaction_id!r} is not a valid '
                  f'transaction ID')

    def set_transaction_type(self, transaction_type):
        if transaction_type in self.TRANSACTION_TYPES:
            self.__transaction_type = transaction_type
        else:
            print(f'Rejected: {transaction_type!r} is not a valid '
                  f'transaction type')

    def set_transaction_amt(self, transaction_amt):
        if is_number(transaction_amt):
            self.__transaction_amt = transaction_amt
        else:
            print(f'Rejected: {transaction_amt!r} is not a valid '
                  f'transaction amount')

    def set_transaction_desc(self, transaction_desc):
        if isinstance(transaction_desc, str):
            self.__transaction_desc = transaction_desc
        else:
            print(f'Rejected: {transaction_desc!r} is not a valid '
                  f'transaction description')

    def __str__(self):
        return (f'Transaction ID: {self.__transaction_id}\n'
                f' Transaction type: {self.__transaction_type}\n'
                f' Amount: {self.__transaction_amt}\n'
                f' Description: {self.__transaction_desc}\n'
                f' Current Status: {self.__status}')

    def __repr__(self):
        return (f'Transaction(Transaction ID={self.__transaction_id!r}, '
                f'Type={self.__transaction_type!r}, '
                f'Amount={self.__transaction_amt!r}, '
                f'Description={self.__transaction_desc!r}, '
                f'Status={self.__status!r})')

    def process_transaction(self, account):
        """Apply this transaction to an Account.

        Returns True when it was applied and the status becomes
        'Processed'. Only a Pending transaction can be processed. If it is
        not, or the Account refuses it (a FinanceError such as
        insufficient funds), the error is reported, the Account is left
        untouched, the status stays as it was and False is returned.
        """
        # Imported here because account.py imports this module, so a
        # top-level import would be circular.
        from account import Account
        if not isinstance(account, Account):
            print(f'Rejected: {account!r} is not a valid Account')
            return False
        try:
            if self.__status != 'Pending':
                raise TransactionStatusError(self.__transaction_id,
                                             self.__status)
            if self.__transaction_type == 'deposit':
                account.deposit(self.__transaction_amt)
            else:
                account.withdrawal(self.__transaction_amt)
        except FinanceError as error:
            print(f'Transaction {self.__transaction_id} failed: {error}')
            return False
        self.__status = 'Processed'
        return True

    def cancel_transaction(self):
        if self.__status == 'Pending':
            self.__status = 'Cancelled'
            print('Transaction is cancelled')
        elif self.__status == 'Processed':
            print('This transaction has already been processed.')
        elif self.__status == 'Cancelled':
            print('This transaction has already been cancelled.')

    def update_transaction(self, transaction_desc):
        """Replace the description; an invalid description is rejected."""
        self.set_transaction_desc(transaction_desc)
