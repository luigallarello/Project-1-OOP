Workshop 2.1, 12/08
In this workshop, we created the transaction and branch classes. At first, I struggled 
to understand the logic for the transaction at first but then realised that it would be 
handling deposits and withdrawl. Our tutor explained it as the account methods could be 
adopted when the classes are imported into main.py. After that explanation I fully understood 
what the goal was.

    def cancel_transaction(self):
            if self.status == "Pending":
                self.status = "Cancelled"
                print('Transaction is cancelled')
            elif self.status == "Processed":
                print("This transaction has already been processed.")

The above piece of code is my cancel transaction method. Upon tutors review, 
there was no condition for if a transaction is already cancelled it can't
go through. I still am yet to add this in but to do it, I will just create a third elif and 
say if the status is already cancelled then don't change the status.

Resulting change (added 31/08, closing this out): added the missing
branch so cancel_transaction() now handles all three statuses:

    elif self.__status == 'Cancelled':
        print('This transaction has already been cancelled.')

main.py now calls cancel_transaction() twice on the same transaction
to prove the second call is handled correctly instead of silently
re-cancelling it. This was sitting unfinished for a few workshops -
good reminder to close the loop on review feedback before moving on
to the next topic, not just note it and leave it.

Workshop 2.2 19/08
This workshop had us making each of the variables become private. This is done using a 
double underscore for each variable that needs to be private. In the code review, the tutor 
suggested that an integer can be assigned to an account number to ensure fairness which is something to note. 
I didn't get around to task 4 onwards so I'm completing that on 21/08.

Resulting change: none made yet - account numbers are still validated
as any non-negative int with no uniqueness/allocation check. Leaving
this as an open item rather than a real fix, since enforcing
uniqueness across Account instances isn't something the current
class can do on its own (it would need something tracking all
issued account numbers, which is out of scope for what's been
taught so far). 

Workshop 3.1 21/08
This workshop I am finishing up what I missed out on in the earlier workshop. 
This includes the first uml, and then coding relationships between classes.

Reviewed in class (forgot to ask for tutors name):

Reviewed: Client.add_account() / Client.remove_account() and the new
Client-Account aggregation.

Discussion: walked through the isinstance() check and the append
logic. The first draft had the branches backwards - it appended when
the object was NOT an Account, and had no rejection message for
invalid types. Also flagged that returning the internal
self.__accounts list directly from a getter breaks encapsulation,
since a caller could mutate it and bypass the type/duplicate checks
entirely.

Why it mattered: this was the first method implementing the new
aggregation requirement, so getting the validation logic right here
set the pattern followed for remove_account and the Branch
association methods after it.

Resulting change: fixed the inverted branch logic so a valid,
non-duplicate account appends correctly and an invalid type is
rejected with a message; changed get_account_list() to
`return self.__accounts.copy()` instead of the raw list, so external
code can read the list but not mutate it directly.

    def add_account(self, account):
        if isinstance(account, Account):
            if account in self.__accounts:
                return 'You already have an account that matches.'
            else:
                self.__accounts.append(account)
        else:
            return 'Not a valid account, please enter an Account'

Result: the aggregation is now actually protected - external code
can read the account list but can't corrupt it, and rejected inputs
no longer silently fall through.

Workshop 3.2 23/08

Reviewed with: (forgot to ask tutors name again)

Reviewed: the whole Topic 3 checkpoint - the UML diagram against the
implementation, encapsulation/validation across all four classes,
Transaction.process_transaction(), and main.py's test coverage.

Discussion: comparing the diagram to the code turned up several
places where the model had drifted - stale method names left over
from before the PEP8 pass (open_Branch, get_branchNo, withdrawl),
wrong attribute visibility (Branch.branch_name shown private when
it's actually public), and a Transaction-Account dependency arrow
drawn pointing the wrong way. Separately, reviewing
process_transaction() showed it never checked isinstance(account,
Account) before calling account.deposit()/account.withdrawal() - the
one account-relationship method that skipped the type check every
other one in the project enforces. That review also caught that the
"amount is negative" branch inside process_transaction() could never
actually run, since __validate_transaction_amt() already forces any
negative amount to 0 at construction time - dead code left over from
before validation was added.

Why it mattered: this was the checkpoint review, so the point was
specifically to check the model and code still describe the same
system, and that validation is applied consistently everywhere a
setter or relationship method exists - not just in the newest code.

Resulting change: added isinstance(account, Account) to
process_transaction() and removed the unreachable dead-code branch;
removed Transaction.set_status() since it let status jump straight
to Processed/Cancelled without going through process_transaction()/
cancel_transaction(), bypassing the only place that logic was
supposed to live; added a short docstring to each of the four
classes describing its responsibility; expanded main.py so every
public method on every class is exercised at least once (previously
several setters/getters, and both __str__/__repr__ on some classes,
were never called anywhere).

    def process_transaction(self, account):
        if not isinstance(account, Account):
            print(f'Rejected: {account!r} is not a valid Account')
            return
        if self.__transaction_type == 'deposit':
            account.deposit(self.__transaction_amt)
            self.__status = 'Processed'
        elif self.__transaction_type == 'withdrawal':
            account.withdrawal(self.__transaction_amt)
            self.__status = 'Processed'

Result: closed the gap between what the diagram claimed and what the
code actually does, and closed the one validation gap left in the
project. The bigger takeaway was that a diagram and a test suite can
both go stale in different ways at the same time - the diagram
lagged behind renames, and main.py's coverage lagged behind new
methods being added - so both need to be checked, not just one.

Workshop 5-1 - Also code review on 9/09:
I recieved feedback on my new account refactor, there would be no account holder
name in the account parent class as savings and everyday become the new objects.
My method rewriting was all ok. I haven't yet added the composition between account and transaction
quite yet. I need to make it so that account creates transactions.

Week 10 - Custom exceptions and final review

Task 1 - Finance exceptions identified

Before this week every broken rule was handled by printing "Rejected: ..."
and returning, so the caller could not tell whether an operation had worked.
Each situation below is a rule that already existed in the project; the table
records what triggers it and what the exception has to tell the caller.

| Situation                                   | Raised by                                   | Information carried                          |
|---------------------------------------------|---------------------------------------------|----------------------------------------------|
| Deposit/withdrawal amount is not a number > 0 | Account.deposit / withdrawal (shared check) | account number, amount, operation            |
| Withdrawal larger than the balance          | Account.withdrawal                          | account number, balance, amount              |
| Savings Account would fall below $100       | SavingsAccount.withdrawal                   | account number, balance, amount, minimum     |
| Everyday Account withdrawal above $1000     | EverydayAccount.withdrawal                  | account number, balance, amount, limit       |
| Account number not held by the Client       | Client.get_account                          | client number, account number                |

Considered and left as they were: constructor/setter validation (invalid
values still fall back to a default, as the earlier workshops required), a
non-Account passed to add_account() (an input-type mistake, still returns
False like the other setters), and a duplicate account number in add_account()
(still returns False, documented in the method).

Task 2 - Custom exceptions (finance_exceptions.py)

    FinanceError(Exception)
    +-- InvalidAmountError
    +-- AccountNotFoundError
    +-- WithdrawalError
        +-- InsufficientFundsError
        +-- MinimumBalanceError
        +-- WithdrawalLimitError

FinanceError lets a caller catch any Finance rule violation at once.
WithdrawalError groups the three ways a withdrawal can fail, because they
all describe the same account, balance and amount. Each exception keeps its
values as attributes as well as in the message, e.g.

    Account 20: withdrawing $2150 from a balance of $2200 would leave $50,
    below the minimum balance of $100

Task 3 - Raising and handling

Raising: the methods that already enforced each rule now raise instead of
printing. Every check happens before the balance or transaction history is
touched, so a failed operation changes nothing (and does not use up a
transaction id).

Handling: Account/SavingsAccount/EverydayAccount only raise. The classes that
need to carry on afterwards catch FinanceError themselves, so main.py has no
try / except:

- Transaction.process_transaction(account): reports the failure, leaves the
  status Pending and returns False. Before this it marked a refused
  withdrawal as Processed, which was a bug: the status said Processed while
  the account had not changed.
- Client.process_transaction(account_number, transaction): new method that
  finds the account and processes the transaction, handling a missing
  account.
- Client.remove_account(number): catches AccountNotFoundError from
  get_account(), reports it and returns None as before.

Behaviour changes to be aware of: get_account() now raises
AccountNotFoundError instead of returning None, and deposit()/withdrawal()
raise instead of printing. The tests were updated to match.

Task 4 - Tests

New tests/test_exceptions.py covers the hierarchy, message contents, the
attributes on each exception, and that a failed operation leaves balances,
transaction history and the Client's account collection unchanged. The
existing Account, Savings, Everyday, Client, Transaction and interaction tests
now use pytest.raises() where the exception propagates. 150 tests pass.

    python3 -m coverage run -m pytest
    python3 -m coverage report

Coverage is 100% across all Finance modules (main.py and tests are omitted
by .coveragerc), including every raise and except path.

Task 5 - Demonstration (main.py)

The old commented-out workshop blocks were removed (Week9 and earlier folders
keep them). The demo now runs one Client with a SavingsAccount and an
EverydayAccount: successful deposits/withdrawals directly and through
Transactions, then one failure for each exception, a check that balances and
histories are unchanged, a retry that succeeds to show the program carries
on, the same withdrawal applied to both account types, history queries, and
removing an account twice.

UML (changes to make to the diagram)

The draw.io diagram and PNGs in this folder are still the Week 8 versions and
have not been updated; the changes needed are below.

    classDiagram
        Exception <|-- FinanceError
        FinanceError <|-- InvalidAmountError
        FinanceError <|-- AccountNotFoundError
        FinanceError <|-- WithdrawalError
        WithdrawalError <|-- InsufficientFundsError
        WithdrawalError <|-- MinimumBalanceError
        WithdrawalError <|-- WithdrawalLimitError
        class Client {
            +get_account(account_number) Account  «raises AccountNotFoundError»
            +remove_account(account_number) Account
            +process_transaction(account_number, transaction) bool
        }
        class Transaction {
            +process_transaction(account) bool
        }
        class Account {
            +deposit(amount)  «raises InvalidAmountError»
            +withdrawal(amount)  «raises InvalidAmountError, InsufficientFundsError»
        }
        class SavingsAccount {
            +withdrawal(amount)  «raises MinimumBalanceError»
        }
        class EverydayAccount {
            +withdrawal(amount)  «raises WithdrawalLimitError»
        }
        Client ..> AccountNotFoundError : raises/handles
        Client ..> Transaction : uses
        Transaction ..> FinanceError : handles
        Account ..> InvalidAmountError : raises
        Account ..> InsufficientFundsError : raises
        SavingsAccount ..> MinimumBalanceError : raises
        EverydayAccount ..> WithdrawalLimitError : raises

Task 6 - Final review

Checked against the code (the rubric itself was not available to check
against, so confirm these against it):
- Encapsulation: private attributes with validated getters/setters on every
  class; Client returns a read-only view of its accounts.
- Inheritance and abstraction: abstract Account with SavingsAccount and
  EverydayAccount.
- Polymorphism: the same withdrawal() call applies each account's own rule.
- Aggregation/association/dependency: Client owns Accounts and has a
  preferred Branch; Transaction depends on Account; Account records
  Transactions.
- Exceptions: hierarchy, raise-before-change, handling inside Finance classes.
- Tests/coverage: 150 passing, 100% coverage.
- Cleanup: commented-out development code removed from main.py, no unused
  imports.
- Still to do: update week8_uml.drawio and re-export the UML PNG (above).
