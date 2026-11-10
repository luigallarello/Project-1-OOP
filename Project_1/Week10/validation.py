"""Shared checks used by the Finance classes to validate input values.

Booleans are rejected everywhere a number is expected, because
isinstance(True, int) is True in Python.
"""


def is_whole_number(value, minimum=0, maximum=None):
    """Return True if value is an int (not a bool) within the range."""
    if not isinstance(value, int) or isinstance(value, bool):
        return False
    return value >= minimum and (maximum is None or value <= maximum)


def is_number(value, minimum=0, inclusive=True):
    """Return True if value is an int or float (not a bool) above minimum.

    Set inclusive to False to require the value to be strictly greater
    than minimum, for example an amount that must be above 0. A minimum
    of None accepts any number.
    """
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        return False
    if minimum is None:
        return True
    return value >= minimum if inclusive else value > minimum


def is_non_empty_string(value):
    """Return True if value is a string with something other than spaces."""
    return isinstance(value, str) and value.strip() != ''
