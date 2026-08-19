class Branch():
    def __init__(self, branch_no, branch_name, location, phone_no, is_open=False):
        self.__branch_no = branch_no
        self.branch_name = branch_name
        self.location = location
        self.phone_no = phone_no
        self.__is_open = is_open

    def get_branchNo(self):
        return self.__branch_no

    def get_is_open(self):
        return self.__is_open

    def set_branch_no(self, branch_no):
        if isinstance(branch_no, int):
            self.__branch_no = branch_no

    def set_phone_no(self, phone_no):
        if isinstance(phone_no, int):
            self.phone_no = phone_no

    def set_branch_name(self, branch_name):
        if isinstance(branch_name, str):
            self.branch_name = branch_name

    def set_location(self, location):
        if isinstance(location, str):
            self.location = location

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

