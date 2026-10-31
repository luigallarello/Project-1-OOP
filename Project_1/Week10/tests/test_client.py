import pytest

from client import Client
from EverydayAccount import EverydayAccount


def test_valid_construction_keeps_values(client):
    assert client.get_client_no() == 234
    assert client.first_name == 'Priya'
    assert client.last_name == 'Singh'
    assert client.get_email() == 'priya@gmail.com'
    assert client.get_age() == 27
    assert client.get_phone_no() == 411222333
    assert client.get_preferred_branch() is None
    assert len(client.get_accounts()) == 0


def test_invalid_constructor_values_fall_back_to_defaults():
    bad = Client(-1, '', '  ', None, 150, 'call me')
    assert bad.get_client_no() == 0
    assert bad.first_name == 'Unknown'
    assert bad.last_name == 'Unknown'
    assert bad.get_email() == 'unknown'
    assert bad.get_age() == 0
    assert bad.get_phone_no() == 0


def test_age_boundaries_are_valid():
    for age in (0, 120):
        assert Client(1, 'A', 'B', 'a@b.c', age, 1).get_age() == age


def test_age_outside_boundaries_is_invalid():
    for age in (-1, 121, 30.5, True):
        assert Client(1, 'A', 'B', 'a@b.c', age, 1).get_age() == 0


def test_setters_accept_valid_values(client):
    client.set_client_no(5)
    client.set_email('new@mail.com')
    client.set_age(40)
    client.set_phone_no(400111222)
    assert client.get_client_no() == 5
    assert client.get_email() == 'new@mail.com'
    assert client.get_age() == 40
    assert client.get_phone_no() == 400111222


def test_setters_reject_invalid_values_and_keep_old_ones(client):
    client.set_client_no(-5)
    client.set_email('   ')
    client.set_age(121)
    client.set_phone_no('abc')
    assert client.get_client_no() == 234
    assert client.get_email() == 'priya@gmail.com'
    assert client.get_age() == 27
    assert client.get_phone_no() == 411222333


def test_str_and_repr_show_client_details(client):
    assert '234' in str(client)
    assert '411222333' in str(client)
    assert 'priya@gmail.com' in repr(client)
    assert 'Singh' in repr(client)


def test_display_contact_info_prints_details(client, capsys):
    client.display_contact_info()
    out = capsys.readouterr().out
    assert 'Priya' in out and 'priya@gmail.com' in out


def test_add_several_accounts(client_with_accounts):
    assert len(client_with_accounts.get_accounts()) == 2


def test_add_account_returns_true(client, savings_account):
    assert client.add_account(savings_account) is True


def test_get_account_by_number_returns_same_object(client_with_accounts,
                                                   savings_account,
                                                   everyday_account):
    assert client_with_accounts.get_account(10) is savings_account
    assert client_with_accounts.get_account(11) is everyday_account


def test_get_missing_account_returns_none(client_with_accounts):
    assert client_with_accounts.get_account(999) is None


def test_duplicate_account_number_is_rejected(client_with_accounts,
                                              savings_account):
    clash = EverydayAccount(5, 10, 'Priya')
    assert client_with_accounts.add_account(clash) is False
    assert client_with_accounts.get_account(10) is savings_account
    assert len(client_with_accounts.get_accounts()) == 2


def test_non_account_is_rejected(client):
    for not_an_account in ('text', 5, None, {}):
        assert client.add_account(not_an_account) is False
    assert len(client.get_accounts()) == 0


def test_accounts_dictionary_is_keyed_by_account_number(client_with_accounts,
                                                         savings_account,
                                                         everyday_account):
    assert dict(client_with_accounts.get_accounts()) == {
        10: savings_account, 11: everyday_account}


def test_accounts_view_cannot_be_modified(client_with_accounts):
    view = client_with_accounts.get_accounts()
    with pytest.raises(TypeError):
        view[50] = EverydayAccount(1, 50, 'X')
    with pytest.raises(TypeError):
        del view[10]
    assert len(client_with_accounts.get_accounts()) == 2


def test_accounts_view_reflects_later_changes(client, savings_account):
    view = client.get_accounts()
    client.add_account(savings_account)
    assert 10 in view


def test_remove_account_returns_and_removes_it(client_with_accounts,
                                               savings_account):
    removed = client_with_accounts.remove_account(10)
    assert removed is savings_account
    assert client_with_accounts.get_account(10) is None
    assert list(client_with_accounts.get_accounts()) == [11]


def test_remove_missing_account_returns_none(client_with_accounts):
    assert client_with_accounts.remove_account(999) is None
    assert len(client_with_accounts.get_accounts()) == 2


def test_removed_account_number_can_be_reused(client_with_accounts):
    client_with_accounts.remove_account(10)
    assert client_with_accounts.add_account(EverydayAccount(5, 10, 'Priya'))


def test_set_preferred_branch_valid(client, branch):
    message = client.set_preferred_branch(branch)
    assert client.get_preferred_branch() is branch
    assert 'preferred branch' in message


def test_set_preferred_branch_invalid_keeps_old_value(client, branch):
    client.set_preferred_branch(branch)
    message = client.set_preferred_branch('Central')
    assert client.get_preferred_branch() is branch
    assert 'Not a valid branch' in message
