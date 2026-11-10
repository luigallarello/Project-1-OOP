"""The shared input checks used by every Finance class."""
import pytest

from validation import is_non_empty_string, is_number, is_whole_number


@pytest.mark.parametrize('value', [0, 1, 120, 10 ** 12])
def test_whole_numbers_are_accepted(value):
    assert is_whole_number(value)


@pytest.mark.parametrize('value', [-1, 1.5, '1', None, True, False, [1]])
def test_non_whole_numbers_are_rejected(value):
    assert not is_whole_number(value)


def test_whole_number_range_is_inclusive():
    assert is_whole_number(0, maximum=120)
    assert is_whole_number(120, maximum=120)
    assert not is_whole_number(121, maximum=120)
    assert not is_whole_number(4, minimum=5)


@pytest.mark.parametrize('value', [0, 0.5, 100, 2.75])
def test_non_negative_numbers_are_accepted(value):
    assert is_number(value)


@pytest.mark.parametrize('value', [-0.1, 'ten', None, True, [5]])
def test_other_values_are_not_numbers(value):
    assert not is_number(value)


def test_exclusive_minimum_rejects_the_minimum_itself():
    assert not is_number(0, inclusive=False)
    assert is_number(0.01, inclusive=False)


def test_no_minimum_accepts_negative_numbers():
    assert is_number(-50, minimum=None)
    assert not is_number(False, minimum=None)


@pytest.mark.parametrize('value', ['a', ' a ', 'Priya Singh'])
def test_non_empty_strings_are_accepted(value):
    assert is_non_empty_string(value)


@pytest.mark.parametrize('value', ['', '   ', None, 5, ['a']])
def test_empty_or_non_strings_are_rejected(value):
    assert not is_non_empty_string(value)
