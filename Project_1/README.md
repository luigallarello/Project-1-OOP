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
