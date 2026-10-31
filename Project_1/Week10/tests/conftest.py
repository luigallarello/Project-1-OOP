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
def pending_deposit():
    """Pending $200 deposit transaction."""
    return Transaction(1, 'deposit', 200, 'Pay')


@pytest.fixture
def pending_withdrawal():
    """Pending $300 withdrawal transaction."""
    return Transaction(2, 'withdrawal', 300, 'Rent')
