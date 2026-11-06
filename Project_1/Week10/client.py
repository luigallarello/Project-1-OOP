from types import MappingProxyType

from account import Account
from branch import Branch
from finance_exceptions import AccountNotFoundError
from transaction import Transaction


class Client:
    """A bank client and their relationships to other objects.

    Owns zero or more Account objects (aggregation), held in a dict
    keyed by account number, and may select
    one Branch as a preferred branch (association). Responsible for
    the client's own contact details plus the rules for adding,
    removing, and reassigning those relationships - not for the
    Account or Branch objects' own internal behaviour.
    """

    def __init__(self, client_no, first_name, last_name, email, age,
                 phone_no):
        self.__client_no = self.__validate_client_no(client_no)
        self.first_name = self.__validate_name(first_name, 'first name')
        self.last_name = self.__validate_name(last_name, 'last name')
        self.__email = self.__validate_email(email)
        self.__age = self.__validate_age(age)
        self.__phone_no = self.__validate_phone_no(phone_no)
        self.__accounts = {}
        self.__preferred_branch = None

    def __validate_client_no(self, client_no):
        if (isinstance(client_no, int) and not isinstance(client_no, bool)
                and client_no >= 0):
            return client_no
        print(f'Invalid Client Number {client_no!r} - defaulting to 0')
        return 0

    def __validate_name(self, name, field_label):
        if isinstance(name, str) and name.strip() != '':
            return name
        print(f'Invalid {field_label} {name!r} - defaulting to "Unknown"')
        return 'Unknown'

    def __validate_email(self, email):
        if isinstance(email, str) and email.strip() != '':
            return email
        print(f'Invalid email {email!r} - defaulting to unknown')
        return 'unknown'

    def __validate_age(self, age):
        if (isinstance(age, int) and not isinstance(age, bool)
                and 0 <= age <= 120):
            return age
        print(f'Invalid age {age!r} - defaulting to 0')
        return 0

    def __validate_phone_no(self, phone_no):
        if (isinstance(phone_no, int) and not isinstance(phone_no, bool)
                and phone_no >= 0):
            return phone_no
        print(f'Invalid phone number {phone_no!r} - defaulting to 0')
        return 0

    def set_client_no(self, client_no):
        if (isinstance(client_no, int) and not isinstance(client_no, bool)
                and client_no >= 0):
            self.__client_no = client_no
        else:
            print(f'Rejected: {client_no!r} is not a valid client number')

    def set_email(self, email):
        if isinstance(email, str) and email.strip() != '':
            self.__email = email
        else:
            print(f'Rejected: {email!r} is not a valid email')

    def set_age(self, age):
        if (isinstance(age, int) and not isinstance(age, bool)
                and 0 <= age <= 120):
            self.__age = age
        else:
            print(f'Rejected: {age!r} is not a valid age')

    def set_phone_no(self, phone_no):
        if (isinstance(phone_no, int) and not isinstance(phone_no, bool)
                and phone_no >= 0):
            self.__phone_no = phone_no
        else:
            print(f'Rejected: {phone_no!r} is not a valid phone number')

    def get_client_no(self):
        return self.__client_no

    def get_email(self):
        return self.__email

    def get_age(self):
        return self.__age

    def get_phone_no(self):
        return self.__phone_no

    def __str__(self):
        return (f'Client Number: {self.get_client_no()}\n'
                f' Client Name: {self.first_name}{self.last_name}\n'
                f' Phone Number: {self.get_phone_no()}')

    def __repr__(self):
        return (f'Client(client number={self.get_client_no()!r}, '
                f'first name={self.first_name!r}, '
                f'last name={self.last_name!r}, '
                f'email={self.get_email()!r}, '
                f'age={self.get_age()!r}, '
                f'phone number={self.get_phone_no()!r})')

    def display_contact_info(self):
        print(f'''Client Number: {self.get_client_no()},\n
            First Name: {self.first_name},\n
            Last Name: {self.last_name},\n
            Email: {self.get_email()},\n
            Age: {self.get_age()},\n
            Phone No: {self.get_phone_no()}''')

    def add_account(self, account):
        """Store an Account under its account number.

        Returns True if added, False if rejected (not an Account, or
        this client already holds an account with that number).
        """
        if not isinstance(account, Account):
            print(f'Rejected: {account!r} is not an Account')
            return False
        number = account.get_account_number()
        if number in self.__accounts:
            print(f'Rejected: client already has an account numbered '
                  f'{number}')
            return False
        self.__accounts[number] = account
        return True

    def get_account(self, account_number):
        """Return the Account with this number.

        Raises AccountNotFoundError if this client does not hold it.
        """
        account = self.__accounts.get(account_number)
        if account is None:
            raise AccountNotFoundError(self.__client_no, account_number)
        return account

    def remove_account(self, account_number):
        """Remove and return the Account with this number.

        If the client does not hold it, the problem is reported, nothing
        changes and None is returned.
        """
        try:
            account = self.get_account(account_number)
        except AccountNotFoundError as error:
            print(error)
            return None
        del self.__accounts[account_number]
        print(f'Account {account_number} successfully removed')
        return account

    def process_transaction(self, account_number, transaction):
        """Apply a Transaction to one of this client's accounts.

        Returns True if it was processed. If the account is not held, or
        the account refuses the transaction, the problem is reported,
        nothing changes and False is returned.
        """
        if not isinstance(transaction, Transaction):
            print(f'Rejected: {transaction!r} is not a Transaction')
            return False
        try:
            account = self.get_account(account_number)
        except AccountNotFoundError as error:
            print(f'Transaction {transaction.get_transaction_id()} '
                  f'failed: {error}')
            return False
        return transaction.process_transaction(account)

    def get_accounts(self):
        """Read-only view of {account number: Account}.

        The internal dict is never handed out; the view cannot be
        modified, and use add_account()/remove_account() to change it.
        """
        return MappingProxyType(self.__accounts)

    def set_preferred_branch(self, preferred_branch):
        if isinstance(preferred_branch, Branch):
            self.__preferred_branch = preferred_branch
            return (f'{self.__preferred_branch} is now set to your '
                    f'preferred branch')
        else:
            return 'Not a valid branch name, please enter a valid branch name'

    def get_preferred_branch(self):
        return self.__preferred_branch
