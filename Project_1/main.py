from client import Client
from transaction import Transaction
from account import Account
from branch import Branch


# Setup - independent objects, created on their own before any
# relationship is formed.
client_1 = Client(231, 'Fahim', 'Dayhan', 'Fahim@gmail.com', 21, 444444444)
client_2 = Client(232, 'Kosta', 'Toulantas', 'Kosta@gmail.com', 18, 44455555)
client_3 = Client(233, 'Nadir', 'Alim', 'Nadir@gmail.com', 18, 4444566666)

account_1 = Account(20, 2, 'Spending', 'Fahim')
account_2 = Account(1000, 3, 'Savings', 'Kosta')
account_3 = Account(150, 4, 'Spending', 'Nadir')

branch_1 = Branch(1, 'Westpac', 'Prospect', 4000002034)
branch_2 = Branch(2, 'BankSA', 'Norwood', 40205060437)
branch_3 = Branch(3, 'Commonwealth Bank', 'Adelaide', 45067082457)


# 1. Encapsulation - read via getters, modify via setters, and
#    confirm behaviour-based methods still change state.
print('Encapsulation')
print(f'Client 1 age (getter): {client_1.get_age()}')
client_1.set_age(22)
print(f'Client 1 age after set_age(22): {client_1.get_age()}')

print(f'Account 1 balance (getter): {account_1.get_current_balance()}')
account_1.deposit(50)
print(f'Account 1 balance after deposit(50): '
      f'{account_1.get_current_balance()}')

print(f'Branch 1 open? (getter): {branch_1.get_is_open()}')
branch_1.open_branch()
print(f'Branch 1 open? after open_branch(): {branch_1.get_is_open()}')


# 2. Validation - valid changes go through, invalid changes are
#    rejected and leave the object's state untouched.
print('\nValidation')
print('-valid changes-')
client_2.set_email('kosta.new@gmail.com')
print(f'Client 2 email: {client_2.get_email()}')
account_2.set_account_type('Term Deposit')
print(f'Account 2 type: {account_2.account_type}')

print('-- invalid changes (rejected, no corruption) --')
client_2.set_age(-5)
print(f'Client 2 age still: {client_2.get_age()}')

account_2.deposit(-100)
print(f'Account 2 balance still: {account_2.get_current_balance()}')

account_2.withdrawal('a lot')
print(f'Account 2 balance still: {account_2.get_current_balance()}')

branch_2.set_phone_no('not-a-number')
print(f'Branch 2 phone still: {branch_2.phone_no}')


# Transaction behaviour - encapsulation and behaviour-based state
# change (status moves from Pending -> Processed/Cancelled).
print('\nTransaction behaviour')
transaction_1 = Transaction(1, 'withdrawal', 300, 'pizza')
transaction_2 = Transaction(2, 'deposit', 1000, 'sushi')

transaction_1.cancel_transaction()
print(f'Transaction 1 status: {transaction_1.get_status()}')
transaction_1.cancel_transaction()  # cancelling twice is now handled

transaction_2.process_transaction(account_2)
print(f'Transaction 2 status: {transaction_2.get_status()}')
print(f'Account 2 balance after processing: '
      f'{account_2.get_current_balance()}')

# 3. Aggregation (Client -- Account)
print('\nAggregation')
client_1.add_account(account_1)
client_2.add_account(account_2)
client_3.add_account(account_3)
print(f'Client 1 accounts: {client_1.get_account_list()}')

print('-- duplicate add rejected --')
print(client_1.add_account(account_1))
print(f'Client 1 still has {len(client_1.get_account_list())} account(s)')

print('-- invalid object rejected --')
print(client_1.add_account('not an account'))
print(f'Client 1 still has {len(client_1.get_account_list())} account(s)')

print('-- remove, then confirm independent lifecycle --')
client_1.remove_account(account_1)
print(f'Client 1 accounts after removal: {client_1.get_account_list()}')
print(f'Account 1 still exists on its own: {account_1}')

# put account_1 back so the coverage section below still has every
# client holding at least one account.
client_1.add_account(account_1)


# 4. Association (Client -- Branch)
print('\nAssociation')
client_1.set_preferred_branch(branch_1)
client_2.set_preferred_branch(branch_2)
print(f'Client 1 preferred branch: {client_1.get_preferred_branch()}')
print(f'Client 2 preferred branch: {client_2.get_preferred_branch()}')

print('-- invalid object rejected --')
print(client_1.set_preferred_branch('Westpac'))
print(f'Client 1 preferred branch unchanged: '
      f'{client_1.get_preferred_branch()}')

print('-- change an existing association --')
client_1.set_preferred_branch(branch_3)
print(f'Client 1 preferred branch now: {client_1.get_preferred_branch()}')
print(f'Client 2 preferred branch unaffected: '
      f'{client_2.get_preferred_branch()}')


# 5. Various methods at work for full coverage
print('\n=== Full method coverage: Client ===')
print(f'Client 3 no (getter): {client_3.get_client_no()}')
client_3.set_client_no(999)
print(f'Client 3 no after set_client_no(999): {client_3.get_client_no()}')

print(f'Client 3 phone (getter): {client_3.get_phone_no()}')
client_3.set_phone_no(999999999)
print(f'Client 3 phone after set_phone_no(...): {client_3.get_phone_no()}')

client_3.display_contact_info()
print(client_1)
print(repr(client_1))

print('\n=== Full method coverage: Account ===')
account_3.set_account_number(9)
print(f'Account 3 number after set_account_number(9): '
      f'{account_3.get_account_number()}')

account_3.set_account_holder_name('N. Alim')
print(f'Account 3 holder after set_account_holder_name(...): '
      f'{account_3.account_holder_name}')

account_3.display_current_balance()
print(repr(account_3))

print('\n=== Full method coverage: Branch ===')
print('-- close_branch() when already closed --')
branch_3.close_branch()
print('-- open then close for real --')
branch_3.open_branch()
branch_3.close_branch()

branch_3.set_branch_no(4)
print(f'Branch 3 no after set_branch_no(4): {branch_3.get_branch_no()}')
branch_3.set_branch_name('NAB')
print(f'Branch 3 name after set_branch_name(...): {branch_3.branch_name}')
branch_3.set_location('Glenelg')
print(f'Branch 3 location after set_location(...): {branch_3.location}')
print(repr(branch_3))

print('\n=== Full method coverage: Transaction ===')
transaction_3 = Transaction(3, 'withdrawal', 4000, 'new car')
print(f'Transaction 3 id: {transaction_3.get_transaction_id()}')
print(f'Transaction 3 type: {transaction_3.get_transaction_type()}')
print(f'Transaction 3 amount: {transaction_3.get_transaction_amt()}')

transaction_3.set_transaction_id(4)
print(f'Transaction 3 id after set_transaction_id(4): '
      f'{transaction_3.get_transaction_id()}')

transaction_3.set_transaction_type('deposit')
print(f'Transaction 3 type after set_transaction_type(...): '
      f'{transaction_3.get_transaction_type()}')

transaction_3.set_transaction_amt(500)
print(f'Transaction 3 amount after set_transaction_amt(500): '
      f'{transaction_3.get_transaction_amt()}')

transaction_3.set_transaction_desc('used car')
print(f'Transaction 3 desc after set_transaction_desc(...): '
      f'{transaction_3.transaction_desc}')

print(transaction_3)
print(repr(transaction_3))

print('-- process_transaction() rejects a non-Account object --')
transaction_3.process_transaction('not an account')
print(f'Transaction 3 status unchanged: {transaction_3.get_status()}')
