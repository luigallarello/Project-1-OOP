"""Shared Account behaviour, exercised through the concrete account types."""
import pytest

from account import Account
from EverydayAccount import EverydayAccount
from finance_exceptions import InsufficientFundsError, InvalidAmountError
from SavingsAccount import SavingsAccount


def test_account_is_abstract():
    with pytest.raises(TypeError):
        Account(100, 1, 'Priya')


def test_valid_construction_keeps_values():
    for account in (SavingsAccount(500, 1, 'Priya', 0.02),
                    EverydayAccount(500, 1, 'Priya')):
        assert account.get_current_balance() == 500
        assert account.get_account_number() == 1
        assert account.account_holder_name == 'Priya'
        assert account.get_transactions() == []


def test_invalid_starting_balance_defaults_to_zero():
    for bad_balance in (-1, 'ten', None, True, [5]):
        account = EverydayAccount(bad_balance, 1, 'Priya')
        assert account.get_current_balance() == 0


def test_invalid_account_number_defaults_to_zero():
    for bad_number in (-1, 1.5, '7', None, True):
        account = EverydayAccount(100, bad_number, 'Priya')
        assert account.get_account_number() == 0


def test_invalid_holder_name_defaults_to_unknown():
    for bad_name in ('', '   ', None, 42):
        account = EverydayAccount(100, 1, bad_name)
        assert account.account_holder_name == 'Unknown'


def test_zero_balance_is_valid():
    assert EverydayAccount(0, 1, 'Priya').get_current_balance() == 0


def test_deposit_increases_balance(everyday_account):
    everyday_account.deposit(250)
    assert everyday_account.get_current_balance() == 1750


def test_deposit_accepts_float(everyday_account):
    everyday_account.deposit(0.5)
    assert everyday_account.get_current_balance() == 1500.5


def test_invalid_deposit_changes_nothing(everyday_account):
    for bad_amount in (0, -50, 'abc', None, True):
        with pytest.raises(InvalidAmountError):
            everyday_account.deposit(bad_amount)
    assert everyday_account.get_current_balance() == 1500
    assert everyday_account.get_transactions() == []


def test_withdrawal_exceeding_balance_is_rejected():
    account = EverydayAccount(500, 1, 'Priya')
    with pytest.raises(InsufficientFundsError):
        account.withdrawal(600)
    assert account.get_current_balance() == 500
    assert account.get_transactions() == []


def test_withdrawal_of_entire_balance_is_allowed():
    account = EverydayAccount(500, 1, 'Priya')
    account.withdrawal(500)
    assert account.get_current_balance() == 0


def test_invalid_withdrawal_changes_nothing(everyday_account):
    for bad_amount in (0, -50, 'abc', None, True):
        with pytest.raises(InvalidAmountError):
            everyday_account.withdrawal(bad_amount)
    assert everyday_account.get_current_balance() == 1500
    assert everyday_account.get_transactions() == []


def test_set_account_number_valid(everyday_account):
    everyday_account.set_account_number(99)
    assert everyday_account.get_account_number() == 99


def test_set_account_number_invalid_keeps_old_value(everyday_account):
    for bad_number in (-1, 2.5, 'x', None, True):
        everyday_account.set_account_number(bad_number)
    assert everyday_account.get_account_number() == 11


def test_set_account_holder_name_valid(everyday_account):
    everyday_account.set_account_holder_name('Mia')
    assert everyday_account.account_holder_name == 'Mia'


def test_set_account_holder_name_invalid_keeps_old_value(everyday_account):
    for bad_name in ('', '  ', None, 5):
        everyday_account.set_account_holder_name(bad_name)
    assert everyday_account.account_holder_name == 'Priya'


def test_str_includes_balance_number_type_and_name(savings_account):
    text = str(savings_account)
    assert '1000' in text
    assert '10' in text
    assert 'Savings' in text
    assert 'Priya' in text


def test_repr_includes_type_and_values(everyday_account):
    text = repr(everyday_account)
    assert 'Everyday' in text
    assert '1500' in text
    assert 'Priya' in text


def test_display_current_balance_prints_balance(everyday_account, capsys):
    everyday_account.display_current_balance()
    assert '1500' in capsys.readouterr().out


def test_base_withdrawal_validates_amount_for_subclasses_that_skip_it():
    # A subclass that delegates straight to Account.withdrawal() relies on
    # the shared validation, so it must still reject bad amounts.
    class PassThroughAccount(Account):
        def get_account_type(self):
            return 'PassThrough'

        def withdrawal(self, withdrawal_amt):
            super().withdrawal(withdrawal_amt)

    account = PassThroughAccount(100, 1, 'Priya')
    with pytest.raises(InvalidAmountError):
        account.withdrawal(-5)
    assert account.get_current_balance() == 100
    account.withdrawal(40)
    assert account.get_current_balance() == 60
