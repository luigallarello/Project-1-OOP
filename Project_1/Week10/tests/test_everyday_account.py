
import pytest

from EverydayAccount import EverydayAccount
from finance_exceptions import (InsufficientFundsError, InvalidAmountError,
                                WithdrawalLimitError)


def test_account_type(everyday_account):
    assert everyday_account.get_account_type() == 'Everyday'


def test_valid_withdrawal_reduces_balance(everyday_account):
    everyday_account.withdrawal(300)
    assert everyday_account.get_current_balance() == 1200


def test_withdrawal_of_exact_maximum_is_allowed(everyday_account):
    everyday_account.withdrawal(EverydayAccount.MAX_WITHDRAWAL)
    assert everyday_account.get_current_balance() == 500


def test_withdrawal_above_maximum_is_rejected(everyday_account):
    with pytest.raises(WithdrawalLimitError):
        everyday_account.withdrawal(1001)
    assert everyday_account.get_current_balance() == 1500


def test_rejected_withdrawal_records_no_transaction(everyday_account):
    with pytest.raises(WithdrawalLimitError):
        everyday_account.withdrawal(2000)
    assert everyday_account.get_transactions() == []


def test_can_withdraw_to_zero_balance():
    account = EverydayAccount(400, 1, 'Priya')
    account.withdrawal(400)
    assert account.get_current_balance() == 0


def test_insufficient_funds_under_maximum_is_rejected():
    account = EverydayAccount(400, 1, 'Priya')
    with pytest.raises(InsufficientFundsError):
        account.withdrawal(500)
    assert account.get_current_balance() == 400


def test_invalid_withdrawal_amount_leaves_balance_unchanged(everyday_account):
    for bad_amount in (0, -10, 'abc', None):
        with pytest.raises(InvalidAmountError):
            everyday_account.withdrawal(bad_amount)
    assert everyday_account.get_current_balance() == 1500


def test_deposit_inherited_from_account(everyday_account):
    everyday_account.deposit(500)
    assert everyday_account.get_current_balance() == 2000
