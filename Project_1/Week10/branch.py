from validation import is_non_empty_string, is_whole_number


class Branch:
    """A physical bank branch and whether it is currently open.

    Owns no other objects. Responsible for its own identity/contact
    details and for its open/closed state, which only changes
    through open_branch()/close_branch() rather than a direct
    setter.
    """

    def __init__(self, branch_no, branch_name, location, phone_no,
                 is_open=False):
        self.__branch_no = self.__validate_branch_no(branch_no)
        self.__branch_name = self.__validate_branch_name(branch_name)
        self.__location = self.__validate_location(location)
        self.__phone_no = self.__validate_phone_no(phone_no)
        self.__is_open = self.__validate_is_open(is_open)

    def __validate_branch_no(self, branch_no):
        if is_whole_number(branch_no):
            return branch_no
        print(f'Invalid branch number {branch_no!r} - defaulting to 0')
        return 0

    def __validate_branch_name(self, branch_name):
        if is_non_empty_string(branch_name):
            return branch_name
        print(f'Invalid branch name {branch_name!r} - '
              f'defaulting to "Unknown"')
        return 'Unknown'

    def __validate_location(self, location):
        if is_non_empty_string(location):
            return location
        print(f'Invalid location {location!r} - defaulting to "Unknown"')
        return 'Unknown'

    def __validate_phone_no(self, phone_no):
        if is_whole_number(phone_no):
            return phone_no
        print(f'Invalid phone number {phone_no!r} - defaulting to 0')
        return 0

    def __validate_is_open(self, is_open):
        if isinstance(is_open, bool):
            return is_open
        print(f'Invalid opening state {is_open!r} - defaulting to False')
        return False

    @property
    def branch_name(self):
        return self.__branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        self.set_branch_name(branch_name)

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.set_location(location)

    @property
    def phone_no(self):
        return self.__phone_no

    @phone_no.setter
    def phone_no(self, phone_no):
        self.set_phone_no(phone_no)

    def get_branch_no(self):
        return self.__branch_no

    def get_is_open(self):
        return self.__is_open

    def set_branch_no(self, branch_no):
        if is_whole_number(branch_no):
            self.__branch_no = branch_no
        else:
            print(f'Rejected: {branch_no!r} is not a valid branch number')

    def set_phone_no(self, phone_no):
        if is_whole_number(phone_no):
            self.__phone_no = phone_no
        else:
            print(f'Rejected: {phone_no!r} is not a valid phone number')

    def set_branch_name(self, branch_name):
        if is_non_empty_string(branch_name):
            self.__branch_name = branch_name
        else:
            print(f'Rejected: {branch_name!r} is not a valid branch name')

    def set_location(self, location):
        if is_non_empty_string(location):
            self.__location = location
        else:
            print(f'Rejected: {location!r} is not a valid location')

    def __str__(self):
        return (f'Branch number: {self.__branch_no}\n'
                f' Name: {self.branch_name}\n'
                f' Phone Number: {self.phone_no}\n'
                f' Opening State: {self.get_is_open()}')

    def __repr__(self):
        return (f'Branch(branch number={self.__branch_no!r}, '
                f'name={self.branch_name!r}, '
                f'location={self.location!r}, '
                f'phone number={self.phone_no!r}, '
                f'opening state={self.get_is_open()!r})')

    def open_branch(self):
        if self.__is_open:
            print('Branch is already open')
        else:
            self.__is_open = True
            print(f'{self.location} {self.branch_name} branch is open.')

    def close_branch(self):
        if self.__is_open is False:
            print('Branch is already closed')
        else:
            self.__is_open = False
            print(f'{self.location} {self.branch_name} branch is closed.')

    def update_phone_no(self, phone_no):
        """Replace the phone number; an invalid number is rejected."""
        self.set_phone_no(phone_no)
