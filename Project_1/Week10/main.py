"""Project 1 demonstration: Client, Account and Transaction working together.

Successful operations and operations that break a Finance rule are both
shown. The Finance classes handle the expected exceptions themselves
(see Client.process_transaction, Transaction.process_transaction and
Client.remove_account), so this script never needs try / except and
simply carries on after each failure.
"""
from client import Client
from EverydayAccount import EverydayAccount
from SavingsAccount import SavingsAccount
from transaction import Transaction


def show_balances(client):
    for number, account in client.get_accounts().items():
        print(f'  {account.get_account_type()} account {number}: '
              f'${account.get_current_balance()} '
              f'({account.get_transaction_count()} transactions)')


print('=== Setting up a Client with both account types ===')
client = Client(235, 'Mia', 'Chen', 'mia@gmail.com', 31, 422333444)
savings = SavingsAccount(2000, 20, 'Mia', 0.03)
everyday = EverydayAccount(800, 21, 'Mia')
client.add_account(savings)
client.add_account(everyday)
# Both of these are rejected: account number 20 is already held, and a
# string is not an Account.
client.add_account(EverydayAccount(10, 20, 'Mia'))
client.add_account('not an account')
print(f'Account numbers held: {list(client.get_accounts())}')
show_balances(client)

print('\n=== Successful operations ===')
# Every deposit and withdrawal goes through Client.process_transaction,
# which handles any Finance exception, so nothing here can stop the demo.
for account_number, transaction in (
        (20, Transaction(1, 'deposit', 500, 'Savings top up')),
        (20, Transaction(2, 'withdrawal', 300, 'Bills')),
        (21, Transaction(3, 'deposit', 200, 'Transfer in')),
        (21, Transaction(4, 'withdrawal', 300, 'Groceries'))):
    client.process_transaction(account_number, transaction)

wages = Transaction(5, 'deposit', 400, 'Wages')
rent = Transaction(6, 'withdrawal', 450, 'Rent')
print(f'Processing {wages.get_transaction_type()} of '
      f'${wages.get_transaction_amt()} on account 21: '
      f'{client.process_transaction(21, wages)}')
print(f'Processing {rent.get_transaction_type()} of '
      f'${rent.get_transaction_amt()} on account 21: '
      f'{client.process_transaction(21, rent)}')
print(f'Transaction statuses: wages={wages.get_status()}, '
      f'rent={rent.get_status()}')
show_balances(client)

print('\n=== Operations that break a Finance rule ===')
print('Everyday account: withdrawal above the $1000 maximum')
too_big = Transaction(7, 'withdrawal', 1200, 'Holiday')
client.process_transaction(21, too_big)

print('\nEveryday account: withdrawal larger than the balance')
overdraw = Transaction(8, 'withdrawal', 900, 'Car repair')
client.process_transaction(21, overdraw)

print('\nSavings account: withdrawal below the $100 minimum balance')
below_minimum = Transaction(9, 'withdrawal', 2150, 'Laptop')
client.process_transaction(20, below_minimum)

print('\nSavings account: invalid amount')
zero_deposit = Transaction(10, 'deposit', 0, 'Nothing')
client.process_transaction(20, zero_deposit)

print('\nAccount number the client does not hold')
client.process_transaction(99, Transaction(11, 'deposit', 50, 'Gift'))

print('\nEvery failed transaction stays Pending:')
for txn in (too_big, overdraw, below_minimum, zero_deposit):
    print(f'  #{txn.get_transaction_id()} {txn.get_status()}')

print('\nBalances and histories are unchanged by the failures:')
show_balances(client)

# The failed transactions above changed nothing, so new ones still work.
print('\n=== The program carries on after the failures ===')
retry = Transaction(12, 'withdrawal', 900, 'Car repair (smaller)')
client.process_transaction(21, Transaction(13, 'deposit', 300, 'Top up'))
client.process_transaction(21, retry)
print(f'Retry status: {retry.get_status()}')

# The same call is made on each account, and each applies its own rule.
print('\n=== Same withdrawal() call, each account applies its own rule ===')
for account in (savings, everyday):
    print(f'{account.get_account_type()}: withdrawing $1050')
    wd = Transaction(14, 'withdrawal', 1050, 'Same request')
    wd.process_transaction(account)

print('\n=== Transaction history (account 21) ===')
for txn in everyday.get_transactions():
    print(f'  #{txn.get_transaction_id()} {txn.get_transaction_type():<10}'
          f' ${txn.get_transaction_amt()}')
withdrawals = everyday.get_transactions_by_type('withdrawal')
print(f'Withdrawals only: {[t.get_transaction_amt() for t in withdrawals]}')
large = everyday.get_transactions_above(300)
print(f'Transactions above $300: {[t.get_transaction_amt() for t in large]}')

print('\n=== Removing accounts ===')
# The second removal is reported as a missing account and the program
# carries on.
client.remove_account(20)
client.remove_account(20)
print(f'Account numbers held: {list(client.get_accounts())}')
print(f'Final balance: ${everyday.get_current_balance()}')
