class Account:
    def __init__(self, currentBalance, accountNumber, accountType, accountHolderName):
        self.__currentBalance = self.__validate_currentBalance(currentBalance)
        self.__accountNumber = self.__validate_accountNumber(accountNumber)
        self.accountType = self.__validate_accountType(accountType)
        self.accountHolderName = self.__validate_accountHolderName(accountHolderName)

    def __validate_currentBalance(self, currentBalance):
        if isinstance(currentBalance, (int, float)) and not isinstance(currentBalance, bool) and currentBalance >= 0:
            return currentBalance
        print(f'Invalid current balance {currentBalance!r} - defaulting to 0')
        return 0

    def __validate_accountNumber(self, accountNumber):
        if isinstance(accountNumber, int) and not isinstance(accountNumber, bool) and accountNumber >= 0:
            return accountNumber
        print(f'Invalid account number {accountNumber!r} - defaulting to 0')
        return 0

    def __validate_accountType(self, accountType):
        if isinstance(accountType, str) and accountType.strip() != '':
            return accountType
        print(f'Invalid account type {accountType!r} - defaulting to "Unknown"')
        return 'Unknown'

    def __validate_accountHolderName(self, accountHolderName):
        if isinstance(accountHolderName, str) and accountHolderName.strip() != '':
            return accountHolderName
        print(f'Invalid account holder name {accountHolderName!r} - defaulting to "Unknown"')
        return 'Unknown'

    def get_currentBalance(self):
        return self.__currentBalance

    def get_accountNumber(self):
        return self.__accountNumber

    def set_accountNumber(self, accountNumber):
        if isinstance(accountNumber, int) and not isinstance(accountNumber, bool) and accountNumber >= 0:
            self.__accountNumber = accountNumber
        else:
            print(f'Rejected: {accountNumber!r} is not a valid account number')

    def set_accountType(self, accountType):
        if isinstance(accountType, str) and accountType.strip() != '':
            self.accountType = accountType
        else:
            print(f'Rejected: {accountType!r} is not a valid account type')

    def set_accountHolderName(self, accountHolderName):
        if isinstance(accountHolderName, str) and accountHolderName.strip() != '':
            self.accountHolderName = accountHolderName
        else:
            print(f'Rejected: {accountHolderName!r} is not a valid account holder name')

    def __str__(self):
            return f'Current Balance: {self.get_currentBalance()}\n Account Number: {self.get_accountNumber()}\n Type: {self.accountType}\n Account Name: {self.accountHolderName}'

    def __repr__(self):
        return f'Account(current balance={self.get_currentBalance()!r}, account number={self.get_accountNumber()!r}, type={self.accountType!r}, account holder name={self.accountHolderName!r})'

    def __validate_amount(self, amount, label):
        if isinstance(amount, (int, float)) and not isinstance(amount, bool) and amount > 0:
            return True
        print(f'Rejected: {amount!r} is not a valid {label} amount')
        return False

    def deposit(self, depositAmt):
        if not self.__validate_amount(depositAmt, 'deposit'):
            return
        self.__currentBalance += depositAmt
        print(f'Your new balance is ${self.__currentBalance}.')

    def withdrawl(self, withdrawlAmt):
        if not self.__validate_amount(withdrawlAmt, 'withdrawal'):
            return
        if withdrawlAmt > self.__currentBalance:
            print(f'Not Enough Funds, you only have ${self.__currentBalance}.')
        else:
            self.__currentBalance -= withdrawlAmt
            print(f'Your new balance is ${self.__currentBalance}.')

    def displayCurrentBalance(self):
        print(f'Your current Balance is ${self.__currentBalance}.')
