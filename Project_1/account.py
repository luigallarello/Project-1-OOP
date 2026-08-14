class Account:
    def __init__(self, currentBalance, accountNumber, accountType, accountHolderName):
        self.currentBalance = currentBalance
        self.accountNumber = accountNumber
        self.accountType = accountType
        self.accountHolderName = accountHolderName

    def __str__(self):
            return f'Current Balance: {self.currentBalance}\n Account Number: {self.accountNumber}\n Type: {self.accountType}\n Account Name: {self.accountHolderName}'
    
    def __repr__(self):
        return f'Client(client number={self.clientNo!r}, first name={self.firstName!r}, last name={self.lastName!r}, email={self.email!r}, age={self.age!r}, phone number={self.phoneNo!r})'
    
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
