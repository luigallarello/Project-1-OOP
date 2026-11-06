
from transaction import Transaction


def test_valid_construction_keeps_values():
    txn = Transaction(5, 'withdrawal', 75.5, 'Groceries', status='Processed')
    assert txn.get_transaction_id() == 5
    assert txn.get_transaction_type() == 'withdrawal'
    assert txn.get_transaction_amt() == 75.5
    assert txn.transaction_desc == 'Groceries'
    assert txn.get_status() == 'Processed'


def test_default_status_is_pending(pending_deposit):
    assert pending_deposit.get_status() == 'Pending'


def test_invalid_id_defaults_to_zero():
    for bad_id in (-1, 1.5, '1', None, True):
        txn = Transaction(bad_id, 'deposit', 10, 'x')
        assert txn.get_transaction_id() == 0


def test_invalid_type_defaults_to_deposit():
    for bad_type in ('transfer', 'Deposit', 5, None):
        txn = Transaction(1, bad_type, 10, 'x')
        assert txn.get_transaction_type() == 'deposit'


def test_invalid_amount_defaults_to_zero():
    for bad_amt in (-5, 'ten', None, True):
        txn = Transaction(1, 'deposit', bad_amt, 'x')
        assert txn.get_transaction_amt() == 0


def test_invalid_description_defaults_to_empty_string():
    assert Transaction(1, 'deposit', 10, 42).transaction_desc == ''


def test_invalid_status_defaults_to_pending():
    for bad_status in ('Done', 'pending', 3, None):
        txn = Transaction(1, 'deposit', 10, 'x', status=bad_status)
        assert txn.get_status() == 'Pending'


def test_setters_accept_valid_values(pending_deposit):
    pending_deposit.set_transaction_id(9)
    pending_deposit.set_transaction_type('withdrawal')
    pending_deposit.set_transaction_amt(15)
    pending_deposit.set_transaction_desc('Changed')
    assert pending_deposit.get_transaction_id() == 9
    assert pending_deposit.get_transaction_type() == 'withdrawal'
    assert pending_deposit.get_transaction_amt() == 15
    assert pending_deposit.transaction_desc == 'Changed'


def test_setters_reject_invalid_values_and_keep_old_ones(pending_deposit):
    pending_deposit.set_transaction_id(-1)
    pending_deposit.set_transaction_type('transfer')
    pending_deposit.set_transaction_amt('lots')
    pending_deposit.set_transaction_desc(None)
    assert pending_deposit.get_transaction_id() == 1
    assert pending_deposit.get_transaction_type() == 'deposit'
    assert pending_deposit.get_transaction_amt() == 200
    assert pending_deposit.transaction_desc == 'Pay'


def test_str_and_repr_describe_the_transaction(pending_deposit):
    for text in (str(pending_deposit), repr(pending_deposit)):
        assert 'deposit' in text
        assert '200' in text
        assert 'Pay' in text
        assert 'Pending' in text


def test_process_deposit_updates_account_and_status(pending_deposit,
                                                    everyday_account):
    pending_deposit.process_transaction(everyday_account)
    assert everyday_account.get_current_balance() == 1700
    assert pending_deposit.get_status() == 'Processed'


def test_process_withdrawal_updates_account_and_status(pending_withdrawal,
                                                       everyday_account):
    pending_withdrawal.process_transaction(everyday_account)
    assert everyday_account.get_current_balance() == 1200
    assert pending_withdrawal.get_status() == 'Processed'


def test_process_returns_true_when_applied(pending_deposit,
                                           everyday_account):
    assert pending_deposit.process_transaction(everyday_account) is True


def test_process_withdrawal_obeys_account_rules(savings_account, capsys):
    txn = Transaction(1, 'withdrawal', 950, 'Too much')
    assert txn.process_transaction(savings_account) is False
    assert savings_account.get_current_balance() == 1000
    assert 'minimum balance of $100' in capsys.readouterr().out


def test_failed_processing_leaves_status_and_account_unchanged(
        everyday_account):
    txn = Transaction(1, 'withdrawal', 5000, 'Too much')
    assert txn.process_transaction(everyday_account) is False
    assert txn.get_status() == 'Pending'
    assert everyday_account.get_current_balance() == 1500
    assert everyday_account.get_transactions() == []


def test_failed_processing_reports_the_account_and_reason(everyday_account,
                                                          capsys):
    Transaction(4, 'withdrawal', 5000, 'Too much').process_transaction(
        everyday_account)
    out = capsys.readouterr().out
    assert 'Transaction 4 failed' in out
    assert 'Account 11' in out


def test_zero_amount_transaction_fails_without_changes(everyday_account):
    txn = Transaction(1, 'deposit', 0, 'Nothing')
    assert txn.process_transaction(everyday_account) is False
    assert txn.get_status() == 'Pending'
    assert everyday_account.get_current_balance() == 1500


def test_process_with_non_account_is_rejected(pending_deposit):
    assert pending_deposit.process_transaction('not an account') is False
    assert pending_deposit.get_status() == 'Pending'


def test_cancel_pending_transaction(pending_deposit):
    pending_deposit.cancel_transaction()
    assert pending_deposit.get_status() == 'Cancelled'


def test_cancel_processed_transaction_is_refused(pending_deposit,
                                                 everyday_account):
    pending_deposit.process_transaction(everyday_account)
    pending_deposit.cancel_transaction()
    assert pending_deposit.get_status() == 'Processed'


def test_cancel_twice_stays_cancelled(pending_deposit, capsys):
    pending_deposit.cancel_transaction()
    capsys.readouterr()
    pending_deposit.cancel_transaction()
    assert pending_deposit.get_status() == 'Cancelled'
    assert 'already been cancelled' in capsys.readouterr().out


def test_update_transaction_uses_user_input(pending_deposit, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: 'Updated note')
    pending_deposit.update_transaction()
    assert pending_deposit.transaction_desc == 'Updated note'
