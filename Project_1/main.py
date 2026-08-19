from client import Client
from transaction import Transaction
from account import Account
from branch import Branch

# Client info, maintenance of current accounts, deposits, withdrawls and transfers

# Client
# Attributes: client no, first name, last name, email, age, phone phone number
# Behaviours: behaviours: update contact info, view accounts, display details


# Account
# Attributes: Current balance, Account Number, Account type, Account Holder Name
# Behaviours: deposit, withdrawl, get balance, transfer


client_1 = Client(231, 'Fahim', 'Dayhan', 'Fahim@gmail.com', 21, 444444444)
client_2 = Client(232, 'Kosta', 'Toulantas', 'Kosta@gmail.com', 18, 44455555)
client_3 = Client(233, 'Nadir', 'Alim', 'Nadir@gmail.com', 18, 4444566666)

client_1.set_age(44)
client_2.firstName = 'Jeff'
client_3.set_email('Nadir.Alim@gmail.com')

print(client_1)
print(client_3)

# # client1.display_contact_info()
# # client2.display_contact_info()

account_1 = Account(20, 2, 'Spending', 'Fahim')
account_2 = Account(1000, 3, 'Savings', 'Kosta')
account_3 = Account(150, 4, 'Spending', 'Nadir')

account_1.deposit(400)
account_2.withdrawl(500)
account_3.withdrawl(200)

account_2.set_accountType('Term Deposit')
print(account_2)

transaction_1 = Transaction(1, "withdrawl", 300, "pizza")
transaction_2 = Transaction(2, "deposit", 1000, 'sushi')
transaction_3 = Transaction(3, "withdrawl", 4000, 'new car',)

transaction_1.cancel_transaction()
transaction_2.process_transaction(account_2)
transaction_3.set_transaction_desc('used car')
print(transaction_3)

branch_1 = Branch(1, 'Westpac', 'Prospect', 4000002034)
branch_2 = Branch(2, 'BankSA', 'Norwood', 40205060437)
branch_3 = Branch(3, 'Commonwealth Bank', 'Adelaide', 45067082457)

branch_1.open_Branch()
branch_2.close_Branch()
branch_3.set_phone_no(812345678)

print(branch_1)
print(repr(branch_1))














