class Account:
    def __init__(self, currentBalance, accountNumber, accountType, accountHolderName):
        self.currentBalance = currentBalance
        self.accountNumber = accountNumber
        self.accountType = accountType
        self.accountHolderName = accountHolderName

    def deposit(self, depositAmt):
        self.currentBalance += depositAmt
        print(f'Your new balance is ${self.currentBalance}.')

    def withdrawl(self, withdrawlAmt):
        if withdrawlAmt > self.currentBalance:
            print(f'Not Enough Funds, you only have ${self.currentBalance}.')
        else:
            self.currentBalance -= withdrawlAmt
            print(f'Your new balance is ${self.currentBalance}.')

    def displayCurrentBalance(self):
        print(f'Your current Balance is ${self.currentBalance}.')
