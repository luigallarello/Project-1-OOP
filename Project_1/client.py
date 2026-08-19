class Client:
    def __init__(self, clientNo, firstName, lastName, email, age, phoneNo):
        self.__clientNo = clientNo
        self.firstName = firstName
        self.lastName = lastName
        self.__email = email
        self.__age = age
        self.__phoneNo = phoneNo

    def set_clientNo(self, clientNo):
        if isinstance(clientNo, int):
            self.__clientNo = clientNo

    def set_email(self, email):
            if isinstance(email, str):
                self.__email = email

    def set_age(self, age):
            if isinstance(age, int):
                self.__age = age

    def set_phoneNo(self, phoneNo):
            if isinstance(phoneNo, int):
                self.__phoneNo = phoneNo

    def get_clientNo(self):
        return self.__clientNo

    def get_email(self):
        return self.__email

    def get_age(self):
        return self.__age

    def get_phoneNo(self):
        return self.__phoneNo
    
        
    def __str__(self):
        return f'Client Number: {self.get_clientNo()}\n Client Name: {self.firstName}{self.lastName}\n Phone Number: {self.get_phoneNo()}'

    def __repr__(self):
        return f'Client(client number={self.get_clientNo()!r}, first name={self.firstName!r}, last name={self.lastName!r}, email={self.get_email()!r}, age={self.get_age()!r}, phone number={self.get_phoneNo()!r})'

    def display_contact_info(self):
        print(f'''Client Number: {self.get_clientNo()},\n
            First Name: {self.firstName},\n
            Last Name: {self.lastName},\n
            Email: {self.get_email()},\n
            Age: {self.get_age()},\n
            Phone No: {self.get_phoneNo()}''')