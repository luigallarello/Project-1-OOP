
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


def test_can_withdraw_to_zero_balance(small_everyday_account):
    small_everyday_account.withdrawal(400)
    assert small_everyday_account.get_current_balance() == 0


def test_empty_account_cannot_withdraw(empty_everyday_account):
    with pytest.raises(InsufficientFundsError):
        empty_everyday_account.withdrawal(1)
    assert empty_everyday_account.get_current_balance() == 0
    assert empty_everyday_account.get_transactions() == []


def test_empty_account_can_receive_a_deposit(empty_everyday_account):
    empty_everyday_account.deposit(75)
    assert empty_everyday_account.get_current_balance() == 75


def test_insufficient_funds_under_maximum_is_rejected(
        small_everyday_account):
    with pytest.raises(InsufficientFundsError):
        small_everyday_account.withdrawal(500)
    assert small_everyday_account.get_current_balance() == 400


def test_invalid_withdrawal_amount_leaves_balance_unchanged(everyday_account):
    for bad_amount in (0, -10, 'abc', None):
        with pytest.raises(InvalidAmountError):
            everyday_account.withdrawal(bad_amount)
    assert everyday_account.get_current_balance() == 1500


def test_deposit_inherited_from_account(everyday_account):
    everyday_account.deposit(500)
    assert everyday_account.get_current_balance() == 2000
