"""Custom Finance exceptions: hierarchy, messages and failed operations."""
import pytest

from EverydayAccount import EverydayAccount
from finance_exceptions import (AccountNotFoundError, FinanceError,
                                InsufficientFundsError, InvalidAmountError,
                                MinimumBalanceError, WithdrawalError,
                                WithdrawalLimitError)
from SavingsAccount import SavingsAccount


def snapshot(account):
    """Everything about an account that a failed operation must not change."""
    return (account.get_current_balance(), account.get_transactions())


@pytest.mark.parametrize('error_class', [
    InvalidAmountError, AccountNotFoundError, WithdrawalError,
    InsufficientFundsError, MinimumBalanceError, WithdrawalLimitError])
def test_every_exception_is_a_finance_error(error_class):
    assert issubclass(error_class, FinanceError)
    assert issubclass(error_class, Exception)


@pytest.mark.parametrize('error_class', [
    InsufficientFundsError, MinimumBalanceError, WithdrawalLimitError])
def test_withdrawal_problems_share_a_parent(error_class):
    assert issubclass(error_class, WithdrawalError)


def test_invalid_amount_error_details():
    error = InvalidAmountError(7, -5, 'deposit')
    assert (error.account_number, error.amount, error.operation) == (
        7, -5, 'deposit')
    assert 'Account 7' in str(error)
    assert '-5' in str(error)
    assert 'deposit' in str(error)


def test_account_not_found_error_details():
    error = AccountNotFoundError(234, 99)
    assert (error.client_no, error.account_number) == (234, 99)
    assert 'Client 234' in str(error)
    assert '99' in str(error)


def test_insufficient_funds_error_details():
    error = InsufficientFundsError(3, 400, 500)
    assert (error.account_number, error.balance, error.amount) == (3, 400, 500)
    for expected in ('Account 3', '$400', '$500'):
        assert expected in str(error)


def test_minimum_balance_error_details():
    error = MinimumBalanceError(3, 1000, 950, 100)
    assert error.minimum_balance == 100
    for expected in ('Account 3', '$1000', '$950', '$50', '$100'):
        assert expected in str(error)


def test_withdrawal_limit_error_details():
    error = WithdrawalLimitError(3, 1500, 2000, 1000)
    assert error.limit == 1000
    for expected in ('Account 3', '$2000', '$1000'):
        assert expected in str(error)


def test_deposit_of_invalid_amount_raises_with_details(everyday_account):
    with pytest.raises(InvalidAmountError) as excinfo:
        everyday_account.deposit(-50)
    assert excinfo.value.account_number == 11
    assert excinfo.value.amount == -50
    assert excinfo.value.operation == 'deposit'


def test_withdrawal_of_invalid_amount_raises_with_details(savings_account):
    with pytest.raises(InvalidAmountError) as excinfo:
        savings_account.withdrawal('abc')
    assert excinfo.value.operation == 'withdrawal'
    assert excinfo.value.account_number == 10


def test_insufficient_funds_raises_with_account_balance_and_amount():
    account = EverydayAccount(400, 5, 'Priya')
    with pytest.raises(InsufficientFundsError) as excinfo:
        account.withdrawal(500)
    assert excinfo.value.account_number == 5
    assert excinfo.value.balance == 400
    assert excinfo.value.amount == 500


def test_savings_minimum_balance_raises_with_limit(savings_account):
    with pytest.raises(MinimumBalanceError) as excinfo:
        savings_account.withdrawal(950)
    assert excinfo.value.account_number == 10
    assert excinfo.value.balance == 1000
    assert excinfo.value.amount == 950
    assert excinfo.value.minimum_balance == SavingsAccount.MINIMUM_BALANCE
    assert '$100' in str(excinfo.value)


def test_everyday_limit_raises_with_limit(everyday_account):
    with pytest.raises(WithdrawalLimitError) as excinfo:
        everyday_account.withdrawal(1001)
    assert excinfo.value.account_number == 11
    assert excinfo.value.amount == 1001
    assert excinfo.value.limit == EverydayAccount.MAX_WITHDRAWAL


def test_withdrawal_errors_can_be_caught_together(accounts):
    for account in accounts:
        with pytest.raises(WithdrawalError):
            account.withdrawal(5000)


@pytest.mark.parametrize('bad_call', [
    lambda account: account.deposit(0),
    lambda account: account.deposit('ten'),
    lambda account: account.withdrawal(-1),
    lambda account: account.withdrawal(5000),
    lambda account: account.withdrawal(1001),
])
def test_failed_operations_never_change_either_account(bad_call, accounts):
    for account in accounts:
        before = snapshot(account)
        try:
            bad_call(account)
        except FinanceError:
            pass
        assert snapshot(account) == before


def test_failed_operation_does_not_stop_later_ones(savings_account):
    with pytest.raises(MinimumBalanceError):
        savings_account.withdrawal(950)
    savings_account.withdrawal(200)
    assert savings_account.get_current_balance() == 800
    assert savings_account.get_transaction_count() == 1


def test_failed_lookup_leaves_client_accounts_and_histories(
        client_with_accounts):
    before = {number: snapshot(account) for number, account
              in client_with_accounts.get_accounts().items()}
    with pytest.raises(AccountNotFoundError):
        client_with_accounts.get_account(999)
    after = {number: snapshot(account) for number, account
             in client_with_accounts.get_accounts().items()}
    assert after == before
