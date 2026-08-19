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

    def set_is_open(self, is_open):
        if isinstance(is_open, (bool, int)):
            self.__is_open = is_open

    def __str__(self):
        return f'Branch number: {self.__branch_no}\n Name: {self.branch_name}\n Phone Number: {self.phone_no}\n Opening State: {self.is_open}'

    def __repr__(self):
        return f'Branch(branch number={self.__branch_no!r}, name={self.branch_name!r}, location={self.location!r}, phone number={self.phone_no!r}, opening state={self.is_open!r})'
    
    def open_Branch(self):
        self.is_open = True
        print(f"{self.location} {self.branch_name} branch is open.")

    def close_Branch(self):
        if self.is_open == False:
            print("Branch is already closed")
        else:
            self.is_open == False
            print(f"{self.location} {self.branch_name} branch is closed.")

    def update_Phone_No(self):
        self.update_Phone_No = int(input("Please enter the new phone number for the branch."))
        # choice = input(f'The branches new phone number is {new_Phone_num}. Is this correct y/n')
        # if choice == 'y':
        #     self.phone_no == new_Phone_num
        #     print('New number confirmed')
        # elif choice == 'n':
        #     int(input("Please enter the new phone number for the branch."))

