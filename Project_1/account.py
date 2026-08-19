class Account:
    def __init__(self, currentBalance, accountNumber, accountType, accountHolderName):
        self.__currentBalance = currentBalance
        self.__accountNumber = accountNumber
        self.accountType = accountType
        self.accountHolderName = accountHolderName

    def get_currentBalance(self):
        return self.__currentBalance

    def get_accountNumber(self):
        return self.__accountNumber

    def __str__(self):
            return f'Current Balance: {self.get_currentBalance()}\n Account Number: {self.get_accountNumber()}\n Type: {self.accountType}\n Account Name: {self.accountHolderName}'

    def __repr__(self):
        return f'Account(current balance={self.get_currentBalance()!r}, account number={self.get_accountNumber()!r}, type={self.accountType!r}, account holder name={self.accountHolderName!r})'

    def deposit(self, depositAmt):
        self.__currentBalance += depositAmt
        print(f'Your new balance is ${self.__currentBalance}.')

    def withdrawl(self, withdrawlAmt):
        if withdrawlAmt > self.__currentBalance:
            print(f'Not Enough Funds, you only have ${self.__currentBalance}.')
        else:
            self.__currentBalance -= withdrawlAmt
            print(f'Your new balance is ${self.__currentBalance}.')

    def displayCurrentBalance(self):
        print(f'Your current Balance is ${self.__currentBalance}.')
