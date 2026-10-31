from client import Client
from account import Account
from transaction import Transaction
from SavingsAccount import SavingsAccount
from EverydayAccount import EverydayAccount


# # Workshop 5-1 Completed (Account is now abstract - see Week 7 below)

# # 1. Create several account objects
# savings_1 = SavingsAccount(1000, 10, 'Priya', 0.02)
# everyday_1 = EverydayAccount(500, 11, 'Priya')

# # 2. Add the specialised accounts to a Client
# client_4 = Client(234, 'Priya', 'Singh', 'priya@gmail.com', 27, 411222333)
# client_4.add_account(savings_1)
# client_4.add_account(everyday_1)
# print(f'Client 4 accounts: {client_4.get_account_list()}')

# # 3. Demonstrate inherited behaviour (deposit, balance, transactions)
# print('\nInherited behaviour')
# savings_1.deposit(200)
# everyday_1.deposit(150)
# print(f'Savings balance: {savings_1.get_current_balance()}')
# print(f'Everyday balance: {everyday_1.get_current_balance()}')

# print('Savings transactions:')
# for txn in savings_1.get_transactions():
#     print(f'  {txn}')

# print('Everyday transactions:')
# for txn in everyday_1.get_transactions():
#     print(f'  {txn}')

# # 4. Demonstrate overridden behaviour (withdrawal rules)
# print('\nOverridden behaviour')
# print('Savings: valid withdrawal')
# savings_1.withdrawal(300)

# print('Savings: withdrawal that breaches the minimum balance')
# savings_1.withdrawal(5000)

# print('Everyday: valid withdrawal')
# everyday_1.withdrawal(100)

# print('Everyday: withdrawal above the maximum withdrawal amount')
# everyday_1.withdrawal(2000)

# # 5. Demonstrate isinstance()
# print('\nisinstance() checks')
# print(f'savings_1 is an Account: {isinstance(savings_1, Account)}')
# print(f'everyday_1 is an Account: {isinstance(everyday_1, Account)}')
# print(f'type(savings_1) is SavingsAccount: '
#       f'{type(savings_1) is SavingsAccount}')
# print(f'type(everyday_1) is EverydayAccount: '
#       f'{type(everyday_1) is EverydayAccount}')


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
