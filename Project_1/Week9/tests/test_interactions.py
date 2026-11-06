"""Interactions between Client, Account and Transaction objects."""
from transaction import Transaction


def test_deposit_creates_transaction_in_history(everyday_account):
    everyday_account.deposit(250)
    history = everyday_account.get_transactions()
    assert len(history) == 1
    assert isinstance(history[0], Transaction)
    assert history[0].get_transaction_type() == 'deposit'
    assert history[0].get_transaction_amt() == 250
    assert history[0].get_status() == 'Processed'


def test_withdrawal_creates_transaction_in_history(everyday_account):
    everyday_account.withdrawal(400)
    history = everyday_account.get_transactions()
    assert len(history) == 1
    assert history[0].get_transaction_type() == 'withdrawal'
    assert history[0].get_transaction_amt() == 400


def test_transactions_stay_in_order_with_sequential_ids(everyday_account):
    everyday_account.deposit(100)
    everyday_account.withdrawal(50)
    everyday_account.deposit(300)
    history = everyday_account.get_transactions()
    assert [t.get_transaction_id() for t in history] == [1, 2, 3]
    assert [t.get_transaction_type() for t in history] == [
        'deposit', 'withdrawal', 'deposit']
    assert [t.get_transaction_amt() for t in history] == [100, 50, 300]


def test_failed_operations_do_not_consume_transaction_ids(everyday_account):
    everyday_account.deposit(100)
    everyday_account.withdrawal(5000)
    everyday_account.deposit(-5)
    everyday_account.deposit(200)
    ids = [t.get_transaction_id() for t in everyday_account.get_transactions()]
    assert ids == [1, 2]


def test_returned_history_is_a_copy(everyday_account):
    everyday_account.deposit(100)
    everyday_account.get_transactions().clear()
    assert everyday_account.get_transaction_count() == 1


def test_each_account_keeps_its_own_history(savings_account, everyday_account):
    savings_account.deposit(100)
    assert savings_account.get_transaction_count() == 1
    assert everyday_account.get_transaction_count() == 0


def test_transaction_count_by_type(everyday_account):
    everyday_account.deposit(100)
    everyday_account.deposit(200)
    everyday_account.withdrawal(50)
    assert everyday_account.get_transaction_count() == 3
    assert everyday_account.get_transaction_count('deposit') == 2
    assert everyday_account.get_transaction_count('withdrawal') == 1


def test_transactions_by_type_filters_in_order(everyday_account):
    everyday_account.deposit(100)
    everyday_account.withdrawal(30)
    everyday_account.deposit(200)
    everyday_account.withdrawal(40)
    withdrawals = everyday_account.get_transactions_by_type('withdrawal')
    assert [t.get_transaction_amt() for t in withdrawals] == [30, 40]


def test_transactions_by_invalid_type_returns_empty_list(everyday_account):
    everyday_account.deposit(100)
    assert everyday_account.get_transactions_by_type('transfer') == []
    assert everyday_account.get_transaction_count('transfer') == 0


def test_transactions_above_amount(everyday_account):
    everyday_account.deposit(100)
    everyday_account.deposit(500)
    everyday_account.withdrawal(250)
    above = everyday_account.get_transactions_above(250)
    assert [t.get_transaction_amt() for t in above] == [500]


def test_transactions_above_invalid_amount_returns_empty_list(everyday_account):
    everyday_account.deposit(100)
    assert everyday_account.get_transactions_above('big') == []
    assert everyday_account.get_transactions_above(True) == []


def test_operate_on_account_retrieved_through_client(client_with_accounts):
    account = client_with_accounts.get_account(11)
    account.deposit(200)
    account.withdrawal(300)
    assert account.get_current_balance() == 1400
    assert client_with_accounts.get_account(11).get_transaction_count() == 2


def test_both_account_types_managed_through_same_client(client_with_accounts):
    for number in (10, 11):
        client_with_accounts.get_account(number).deposit(100)
    assert client_with_accounts.get_account(10).get_current_balance() == 1100
    assert client_with_accounts.get_account(11).get_current_balance() == 1600


def test_removed_account_keeps_its_state(client_with_accounts):
    client_with_accounts.get_account(10).deposit(100)
    removed = client_with_accounts.remove_account(10)
    assert removed.get_current_balance() == 1100
    assert removed.get_transaction_count() == 1


def test_polymorphic_withdrawal_applies_each_accounts_own_rule(accounts):
    # 950 breaches the savings minimum ($100) but is under the everyday
    # maximum ($1000); no type checks - each account decides for itself.
    for account in accounts:
        account.withdrawal(950)
    balances = [account.get_current_balance() for account in accounts]
    assert balances == [1000, 550]


def test_polymorphic_large_withdrawal(accounts):
    # 1200 is allowed by savings' rules only if the balance stays above $100,
    # and breaks everyday's per-transaction maximum.
    for account in accounts:
        account.deposit(500)
        account.withdrawal(1200)
    balances = [account.get_current_balance() for account in accounts]
    assert balances == [300, 2000]


def test_polymorphic_account_types_are_distinct(accounts):
    assert [a.get_account_type() for a in accounts] == ['Savings', 'Everyday']


def test_process_transactions_against_client_account(client_with_accounts,
                                                     pending_deposit,
                                                     pending_withdrawal):
    account = client_with_accounts.get_account(11)
    pending_deposit.process_transaction(account)
    pending_withdrawal.process_transaction(account)
    assert account.get_current_balance() == 1400
    assert pending_deposit.get_status() == 'Processed'
    assert pending_withdrawal.get_status() == 'Processed'
    assert account.get_transaction_count() == 2
