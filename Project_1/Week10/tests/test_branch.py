
from branch import Branch


def test_valid_construction_keeps_values(branch):
    assert branch.get_branch_no() == 1
    assert branch.branch_name == 'Central'
    assert branch.location == 'Sydney'
    assert branch.phone_no == 291234567
    assert branch.get_is_open() is False


def test_invalid_constructor_values_fall_back_to_defaults():
    bad = Branch(-1, '', ' ', 'phone', is_open='yes')
    assert bad.get_branch_no() == 0
    assert bad.branch_name == 'Unknown'
    assert bad.location == 'Unknown'
    assert bad.phone_no == 0
    assert bad.get_is_open() is False


def test_can_be_created_open():
    assert Branch(1, 'A', 'B', 1, is_open=True).get_is_open() is True


def test_open_then_close_branch(branch):
    branch.open_branch()
    assert branch.get_is_open() is True
    branch.close_branch()
    assert branch.get_is_open() is False


def test_closing_closed_branch_reports_already_closed(branch, capsys):
    branch.close_branch()
    assert branch.get_is_open() is False
    assert 'already closed' in capsys.readouterr().out


def test_setters_accept_valid_values(branch):
    branch.set_branch_no(7)
    branch.set_phone_no(299999999)
    branch.set_branch_name('North')
    branch.set_location('Perth')
    assert branch.get_branch_no() == 7
    assert branch.phone_no == 299999999
    assert branch.branch_name == 'North'
    assert branch.location == 'Perth'


def test_setters_reject_invalid_values_and_keep_old_ones(branch):
    branch.set_branch_no(-1)
    branch.set_phone_no('x')
    branch.set_branch_name('')
    branch.set_location(None)
    assert branch.get_branch_no() == 1
    assert branch.phone_no == 291234567
    assert branch.branch_name == 'Central'
    assert branch.location == 'Sydney'


def test_str_and_repr_show_branch_details(branch):
    assert 'Central' in str(branch)
    assert 'Sydney' in repr(branch)


def test_update_phone_no_replaces_the_number(branch):
    branch.update_phone_no(288888888)
    assert branch.phone_no == 288888888


def test_update_phone_no_rejects_invalid_number(branch, capsys):
    branch.update_phone_no('call me')
    assert branch.phone_no == 291234567
    assert 'not a valid phone number' in capsys.readouterr().out


def test_attributes_cannot_bypass_validation(branch):
    branch.phone_no = 'bad'
    branch.branch_name = ''
    branch.location = None
    assert branch.phone_no == 291234567
    assert branch.branch_name == 'Central'
    assert branch.location == 'Sydney'


def test_attributes_accept_valid_assignment(branch):
    branch.phone_no = 299999999
    branch.branch_name = 'Harbour'
    branch.location = 'Newcastle'
    assert (branch.phone_no, branch.branch_name, branch.location) == (
        299999999, 'Harbour', 'Newcastle')


def test_open_branch_fixture_is_open(open_branch):
    assert open_branch.get_is_open() is True


def test_open_branch_can_be_closed(open_branch):
    open_branch.close_branch()
    assert open_branch.get_is_open() is False


def test_opening_an_open_branch_keeps_it_open(open_branch, capsys):
    open_branch.open_branch()
    assert open_branch.get_is_open() is True
    assert 'already open' in capsys.readouterr().out
