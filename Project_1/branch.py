class Branch():
    def __init__(self, branch_no, branch_name, location, phone_no, is_open=False):
        self.__branch_no = self.__validate_branch_no(branch_no)
        self.branch_name = self.__validate_branch_name(branch_name)
        self.location = self.__validate_location(location)
        self.phone_no = self.__validate_phone_no(phone_no)
        self.__is_open = self.__validate_is_open(is_open)

    def __validate_branch_no(self, branch_no):
        if isinstance(branch_no, int) and not isinstance(branch_no, bool) and branch_no >= 0:
            return branch_no
        print(f'Invalid branch number {branch_no!r} - defaulting to 0')
        return 0

    def __validate_branch_name(self, branch_name):
        if isinstance(branch_name, str) and branch_name.strip() != '':
            return branch_name
        print(f'Invalid branch name {branch_name!r} - defaulting to "Unknown"')
        return 'Unknown'

    def __validate_location(self, location):
        if isinstance(location, str) and location.strip() != '':
            return location
        print(f'Invalid location {location!r} - defaulting to "Unknown"')
        return 'Unknown'

    def __validate_phone_no(self, phone_no):
        if isinstance(phone_no, int) and not isinstance(phone_no, bool) and phone_no >= 0:
            return phone_no
        print(f'Invalid phone number {phone_no!r} - defaulting to 0')
        return 0

    def __validate_is_open(self, is_open):
        if isinstance(is_open, bool):
            return is_open
        print(f'Invalid opening state {is_open!r} - defaulting to False')
        return False

    def get_branchNo(self):
        return self.__branch_no

    def get_is_open(self):
        return self.__is_open

    def set_branch_no(self, branch_no):
        if isinstance(branch_no, int) and not isinstance(branch_no, bool) and branch_no >= 0:
            self.__branch_no = branch_no
        else:
            print(f'Rejected: {branch_no!r} is not a valid branch number')

    def set_phone_no(self, phone_no):
        if isinstance(phone_no, int) and not isinstance(phone_no, bool) and phone_no >= 0:
            self.phone_no = phone_no
        else:
            print(f'Rejected: {phone_no!r} is not a valid phone number')

    def set_branch_name(self, branch_name):
        if isinstance(branch_name, str) and branch_name.strip() != '':
            self.branch_name = branch_name
        else:
            print(f'Rejected: {branch_name!r} is not a valid branch name')

    def set_location(self, location):
        if isinstance(location, str) and location.strip() != '':
            self.location = location
        else:
            print(f'Rejected: {location!r} is not a valid location')

    def __str__(self):
        return f'Branch number: {self.__branch_no}\n Name: {self.branch_name}\n Phone Number: {self.phone_no}\n Opening State: {self.get_is_open()}'

    def __repr__(self):
        return f'Branch(branch number={self.__branch_no!r}, name={self.branch_name!r}, location={self.location!r}, phone number={self.phone_no!r}, opening state={self.get_is_open()!r})'

    def open_Branch(self):
        self.__is_open = True
        print(f"{self.location} {self.branch_name} branch is open.")

    def close_Branch(self):
        if self.__is_open == False:
            print("Branch is already closed")
        else:
            self.__is_open = False
            print(f"{self.location} {self.branch_name} branch is closed.")

    def update_Phone_No(self):
        self.set_phone_no(int(input("Please enter the new phone number for the branch: ")))

