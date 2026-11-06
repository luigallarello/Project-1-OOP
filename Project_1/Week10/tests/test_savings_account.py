import pytest

from finance_exceptions import InvalidAmountError, MinimumBalanceError
from SavingsAccount import SavingsAccount


def test_account_type(savings_account):
    assert savings_account.get_account_type() == 'Savings'


def test_interest_rate_stored_as_float(savings_account):
    assert savings_account.get_interest_rate() == pytest.approx(0.02)


def test_integer_interest_rate_converted_to_float():
    account = SavingsAccount(500, 1, 'Priya', 1)
    assert account.get_interest_rate() == 1.0
    assert isinstance(account.get_interest_rate(), float)


def test_set_interest_rate_valid(savings_account):
    assert savings_account.set_interest_rate(0.05) is True
    assert savings_account.get_interest_rate() == pytest.approx(0.05)


def test_zero_interest_rate_is_valid(savings_account):
    assert savings_account.set_interest_rate(0) is True
    assert savings_account.get_interest_rate() == 0.0


def test_set_interest_rate_invalid_keeps_old_rate(savings_account):
    for bad_rate in (-0.1, 'high', None, True):
        assert savings_account.set_interest_rate(bad_rate) is False
    assert savings_account.get_interest_rate() == pytest.approx(0.02)


def test_valid_withdrawal_reduces_balance(savings_account):
    savings_account.withdrawal(300)
    assert savings_account.get_current_balance() == 700


def test_withdrawal_down_to_exact_minimum_is_allowed(savings_account):
    savings_account.withdrawal(900)
    assert savings_account.get_current_balance() == SavingsAccount.MINIMUM_BALANCE


def test_withdrawal_below_minimum_is_rejected(savings_account):
    with pytest.raises(MinimumBalanceError):
        savings_account.withdrawal(901)
    assert savings_account.get_current_balance() == 1000


def test_rejected_withdrawal_records_no_transaction(savings_account):
    with pytest.raises(MinimumBalanceError):
        savings_account.withdrawal(5000)
    assert savings_account.get_transactions() == []


def test_invalid_withdrawal_amount_leaves_balance_unchanged(savings_account):
    for bad_amount in (0, -10, 'abc', None):
        with pytest.raises(InvalidAmountError):
            savings_account.withdrawal(bad_amount)
    assert savings_account.get_current_balance() == 1000


def test_balance_under_minimum_cannot_withdraw_anything():
    account = SavingsAccount(50, 1, 'Priya', 0.02)
    with pytest.raises(MinimumBalanceError):
        account.withdrawal(1)
    assert account.get_current_balance() == 50


def test_deposit_inherited_from_account(savings_account):
    savings_account.deposit(200)
    assert savings_account.get_current_balance() == 1200
