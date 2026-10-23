from client import Client
from account import Account
from transaction import Transaction
from SavingsAccount import SavingsAccount
from EverydayAccount import EverydayAccount


# Workshop 5-1 Completed (Account is abstract - see Week 7 below)

# 1. Create several account objects
savings_1 = SavingsAccount(1000, 10, 'Priya', 0.02)
everyday_1 = EverydayAccount(500, 11, 'Priya')

# 2. Add the specialised accounts to a Client
client_4 = Client(234, 'Priya', 'Singh', 'priya@gmail.com', 27, 411222333)
client_4.add_account(savings_1)
client_4.add_account(everyday_1)
print(f'Client 4 accounts: {dict(client_4.get_accounts())}')

# 3. Demonstrate inherited behaviour (deposit, balance, transactions)
print('\nInherited behaviour')
savings_1.deposit(200)
everyday_1.deposit(150)
print(f'Savings balance: {savings_1.get_current_balance()}')
print(f'Everyday balance: {everyday_1.get_current_balance()}')

print('Savings transactions:')
for txn in savings_1.get_transactions():
    print(f'  {txn}')

print('Everyday transactions:')
for txn in everyday_1.get_transactions():
    print(f'  {txn}')

# 4. Demonstrate overridden behaviour (withdrawal rules)
print('\nOverridden behaviour')
print('Savings: valid withdrawal')
savings_1.withdrawal(300)

print('Savings: withdrawal that breaches the minimum balance')
savings_1.withdrawal(5000)

print('Everyday: valid withdrawal')
everyday_1.withdrawal(100)

print('Everyday: withdrawal above the maximum withdrawal amount')
everyday_1.withdrawal(2000)

# 5. Demonstrate isinstance()
print('\nisinstance() checks')
print(f'savings_1 is an Account: {isinstance(savings_1, Account)}')
print(f'everyday_1 is an Account: {isinstance(everyday_1, Account)}')
print(f'type(savings_1) is SavingsAccount: '
      f'{type(savings_1) is SavingsAccount}')
print(f'type(everyday_1) is EverydayAccount: '
      f'{type(everyday_1) is EverydayAccount}')


# Week 7 - Abstract Account and polymorphism
#
# Account is abstract (ABC), so it is never created directly - only the
# concrete SavingsAccount and EverydayAccount are. Both are held in one
# list and the SAME withdrawal() call is made on each, with no type
# checks. Python picks each object's own rule at run time:
#   SavingsAccount  - balance may not drop below $100 minimum
#   EverydayAccount - a single withdrawal may not exceed $1000
print('\nPolymorphism: same withdrawal() call, different rules')
accounts = [
    SavingsAccount(1500, 12, 'Priya', 0.02),
    EverydayAccount(1500, 13, 'Priya'),
]

for amount in (1200, 250):
    print(f'\nWithdrawing ${amount} from every account')
    for account in accounts:
        print(f'{account.get_account_type()}:')
        account.withdrawal(amount)

print('\nFinal balances')
for account in accounts:
    print(f'{account.get_account_type()}: '
          f'${account.get_current_balance()}')


# Week 8 - Data structures
#
# Client holds its accounts in a dict keyed by account number. Account
# keeps its transactions in a list, oldest first. Both are reached only
# through methods, never as the raw internal collection.
print('\n\nWeek 8: client.accounts (dict) and account history (list)')
client_5 = Client(235, 'Mia', 'Chen', 'mia@gmail.com', 31, 422333444)
client_5.add_account(SavingsAccount(2000, 20, 'Mia', 0.03))
client_5.add_account(EverydayAccount(800, 21, 'Mia'))

print('\nControlled access to the accounts dict')
client_5.add_account(EverydayAccount(10, 20, 'Mia'))
client_5.add_account('not an account')
print(f'Account numbers held: {list(client_5.get_accounts())}')
try:
    client_5.get_accounts()[99] = 'tampering'
except TypeError as error:
    print(f'Read-only view blocks changes: {error}')
client_5.get_account(99)

# Get an account through the client, then make several transactions
account = client_5.get_account(21)
print(f'\nUsing account {account.get_account_number()} '
      f'({account.get_account_type()}) found via the client')
account.deposit(200)
account.deposit(50)
account.withdrawal(300)
account.withdrawal(5000)
account.withdrawal(120)
account.deposit(900)
account.withdrawal(1000)

# Processing the history
print('\nFull history, in the order it happened')
for txn in account.get_transactions():
    print(f'  #{txn.get_transaction_id()} {txn.get_transaction_type():<10}'
          f' ${txn.get_transaction_amt()}')

print(f'\nTotal transactions: {account.get_transaction_count()}')
print(f'Deposits: {account.get_transaction_count("deposit")}, '
      f'withdrawals: {account.get_transaction_count("withdrawal")}')

print('Withdrawals only:')
for txn in account.get_transactions_by_type('withdrawal'):
    print(f'  #{txn.get_transaction_id()} ${txn.get_transaction_amt()}')

print('Transactions above $250:')
for txn in account.get_transactions_above(250):
    print(f'  #{txn.get_transaction_id()} {txn.get_transaction_type()} '
          f'${txn.get_transaction_amt()}')

print(f'Final balance: ${account.get_current_balance()}')

print('\nInvalid history requests are rejected')
account.get_transactions_by_type('transfer')
account.get_transactions_above('big')

print('\nRemoving an account by number')
client_5.remove_account(20)
client_5.remove_account(20)
print(f'Account numbers held: {list(client_5.get_accounts())}')
