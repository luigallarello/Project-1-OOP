import pytest

from branch import Branch
from client import Client
from EverydayAccount import EverydayAccount
from SavingsAccount import SavingsAccount
from transaction import Transaction


@pytest.fixture
def savings_account():
    """Savings account holding $1000 (minimum balance is $100)."""
    return SavingsAccount(1000, 10, 'Priya', 0.02)


@pytest.fixture
def everyday_account():
    """Everyday account holding $1500 (max single withdrawal is $1000)."""
    return EverydayAccount(1500, 11, 'Priya')


@pytest.fixture
def savings_at_minimum():
    """Savings account sitting exactly on its $100 minimum balance."""
    return SavingsAccount(100, 12, 'Mia', 0.03)


@pytest.fixture
def savings_below_minimum():
    """Savings account already under its minimum balance ($50)."""
    return SavingsAccount(50, 13, 'Mia', 0.03)


@pytest.fixture
def empty_everyday_account():
    """Everyday account with nothing in it."""
    return EverydayAccount(0, 14, 'Mia')


@pytest.fixture
def small_everyday_account():
    """Everyday account holding $400, well under its withdrawal maximum."""
    return EverydayAccount(400, 15, 'Mia')


@pytest.fixture
def accounts(savings_account, everyday_account):
    """One of each concrete account type, for polymorphism tests."""
    return [savings_account, everyday_account]


@pytest.fixture
def client():
    """Client holding no accounts."""
    return Client(234, 'Priya', 'Singh', 'priya@gmail.com', 27, 411222333)


@pytest.fixture
def client_with_accounts(client, savings_account, everyday_account):
    """Client holding the savings (#10) and everyday (#11) accounts."""
    client.add_account(savings_account)
    client.add_account(everyday_account)
    return client


@pytest.fixture
def branch():
    """A closed branch."""
    return Branch(1, 'Central', 'Sydney', 291234567)


@pytest.fixture
def open_branch():
    """An open branch."""
    return Branch(2, 'North', 'Perth', 291234568, is_open=True)


@pytest.fixture
def pending_deposit():
    """Pending $200 deposit transaction."""
    return Transaction(1, 'deposit', 200, 'Pay')


@pytest.fixture
def pending_withdrawal():
    """Pending $300 withdrawal transaction."""
    return Transaction(2, 'withdrawal', 300, 'Rent')


@pytest.fixture
def cancelled_transaction():
    """Cancelled $50 deposit transaction."""
    return Transaction(3, 'deposit', 50, 'Gift', status='Cancelled')
