class Account:
    """A single bank account and its balance.

    Owns no other objects. Responsible for validating and mutating
    its own balance through deposit() and withdrawal(), and for
    reporting its own state - it has no knowledge of which Client
    (if any) currently holds it.
    """

    def __init__(self, current_balance, account_number,account_holder_name):
        self._current_balance = self.__validate_current_balance(
            current_balance)
        self._account_number = self.__validate_account_number(
            account_number)
        self.account_holder_name = self.__validate_account_holder_name(
            account_holder_name)

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
                f' Type: {self.account_type}\n'
                f' Account Name: {self.account_holder_name}')

    def __repr__(self):
        return (f'Account(current balance={self.get_current_balance()!r}, '
                f'account number={self.get_account_number()!r}, '
                f'type={self.account_type!r}, '
                f'account holder name={self.account_holder_name!r})')

    def __validate_amount(self, amount, label):
        if (isinstance(amount, (int, float))
                and not isinstance(amount, bool) and amount > 0):
            return True
        print(f'Rejected: {amount!r} is not a valid {label} amount')
        return False

    def deposit(self, deposit_amt):
        if not self.__validate_amount(deposit_amt, 'deposit'):
            return
        self.__current_balance += deposit_amt
        print(f'Your new balance is ${self.__current_balance}.')

    def _withdrawal(self, withdrawal_amt):
        if not self.__validate_amount(withdrawal_amt, 'withdrawal'):
            return
        if withdrawal_amt > self.__current_balance:
            print(f'Not Enough Funds, you only have '
                  f'${self.__current_balance}.')
        else:
            self.__current_balance -= withdrawal_amt
            print(f'Your new balance is ${self.__current_balance}.')

    def display_current_balance(self):
        print(f'Your current Balance is ${self.__current_balance}.')

    
            

           



        
