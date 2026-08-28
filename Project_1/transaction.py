class Transaction:
    def __init__(self, transaction_id, transaction_type, transaction_amt,
                 transaction_desc, status='Pending'):
        self.__transaction_id = self.__validate_transaction_id(
            transaction_id)
        self.__transaction_type = self.__validate_transaction_type(
            transaction_type)
        self.__transaction_amt = self.__validate_transaction_amt(
            transaction_amt)
        self.transaction_desc = self.__validate_transaction_desc(
            transaction_desc)
        self.__status = self.__validate_status(status)

    def __validate_transaction_id(self, transaction_id):
        if (isinstance(transaction_id, int)
                and not isinstance(transaction_id, bool)
                and transaction_id >= 0):
            return transaction_id
        print(f'Invalid transaction ID {transaction_id!r} - '
              f'defaulting to 0')
        return 0

    def __validate_transaction_type(self, transaction_type):
        if (isinstance(transaction_type, str)
                and transaction_type in ('deposit', 'withdrawal')):
            return transaction_type
        print(f'Invalid transaction type {transaction_type!r} - '
              f'defaulting to "deposit"')
        return 'deposit'

    def __validate_transaction_amt(self, transaction_amt):
        if (isinstance(transaction_amt, (int, float))
                and not isinstance(transaction_amt, bool)
                and transaction_amt >= 0):
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
        if (isinstance(status, str)
                and status in ('Pending', 'Processed', 'Cancelled')):
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

    def set_transaction_id(self, transaction_id):
        if (isinstance(transaction_id, int)
                and not isinstance(transaction_id, bool)
                and transaction_id >= 0):
            self.__transaction_id = transaction_id
        else:
            print(f'Rejected: {transaction_id!r} is not a valid '
                  f'transaction ID')

    def set_transaction_type(self, transaction_type):
        if (isinstance(transaction_type, str)
                and transaction_type in ('deposit', 'withdrawal')):
            self.__transaction_type = transaction_type
        else:
            print(f'Rejected: {transaction_type!r} is not a valid '
                  f'transaction type')

    def set_transaction_amt(self, transaction_amt):
        if (isinstance(transaction_amt, (int, float))
                and not isinstance(transaction_amt, bool)
                and transaction_amt >= 0):
            self.__transaction_amt = transaction_amt
        else:
            print(f'Rejected: {transaction_amt!r} is not a valid '
                  f'transaction amount')

    def set_status(self, status):
        if (isinstance(status, str)
                and status in ('Pending', 'Processed', 'Cancelled')):
            self.__status = status
        else:
            print(f'Rejected: {status!r} is not a valid status')

    def set_transaction_desc(self, transaction_desc):
        if isinstance(transaction_desc, str):
            self.transaction_desc = transaction_desc
        else:
            print(f'Rejected: {transaction_desc!r} is not a valid '
                  f'transaction description')

    def __str__(self):
        return (f'Transaction ID: {self.__transaction_id}\n'
                f' Transaction type: {self.__transaction_type}\n'
                f' Amount: {self.__transaction_amt}\n'
                f' Description: {self.transaction_desc}\n'
                f' Current Status: {self.__status}')

    def __repr__(self):
        return (f'Transaction(Transaction ID={self.__transaction_id!r}, '
                f'Type={self.__transaction_type!r}, '
                f'Amount={self.__transaction_amt!r}, '
                f'Description={self.transaction_desc!r}, '
                f'Status={self.__status!r})')

    def process_transaction(self, account):
        if self.__transaction_type == 'deposit':
            if self.__transaction_amt < 0:
                self.__transaction_amt = int(
                    input('Please enter a valid number:'))
            else:
                account.deposit(self.__transaction_amt)
                self.__status = 'Processed'
        elif self.__transaction_type == 'withdrawal':
            account.withdrawal(self.__transaction_amt)
            self.__status = 'Processed'

    def cancel_transaction(self):
        if self.__status == 'Pending':
            self.__status = 'Cancelled'
            print('Transaction is cancelled')
        elif self.__status == 'Processed':
            print('This transaction has already been processed.')

    def update_transaction(self):
        self.set_transaction_desc(
            input('Please update transaction description: '))
