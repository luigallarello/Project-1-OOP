class Client:
    def __init__(self, clientNo, firstName, lastName, email, age, phoneNo):
        self.__clientNo = self.__validate_clientNo(clientNo)
        self.firstName = self.__validate_name(firstName, 'first name')
        self.lastName = self.__validate_name(lastName, 'last name')
        self.__email = self.__validate_email(email)
        self.__age = self.__validate_age(age)
        self.__phoneNo = self.__validate_phoneNo(phoneNo)

    def __validate_clientNo(self, clientNo):
        if isinstance(clientNo, int) and not isinstance(clientNo, bool) and clientNo >= 0:
            return clientNo
        print(f'Invalid Client Number {clientNo!r} - defaulting to 0')
        return 0

    def __validate_name(self, name, fieldLabel):
        if isinstance(name, str) and name.strip() != '':
            return name
        print(f'Invalid {fieldLabel} {name!r} - defaulting to "Unknown"')
        return 'Unknown'

    def __validate_email(self, email):
        if isinstance(email, str) and email.strip() != '':
            return email
        print(f'Invalid email {email!r} - defaulting to unknown')
        return 'unknown'

    def __validate_age(self, age):
        if isinstance(age, int) and not isinstance(age, bool) and 0 <= age <= 120:
            return age
        print(f'Invalid age {age!r} - defaulting to 0')
        return 0

    def __validate_phoneNo(self, phoneNo):
        if isinstance(phoneNo, int) and not isinstance(phoneNo, bool) and phoneNo >= 0:
            return phoneNo
        print(f'Invalid phone number {phoneNo!r} - defaulting to 0')
        return 0

    def set_clientNo(self, clientNo):
        if isinstance(clientNo, int) and not isinstance(clientNo, bool) and clientNo >= 0:
            self.__clientNo = clientNo
        else:
            print(f'Rejected: {clientNo!r} is not a valid client number')

    def set_email(self, email):
        if isinstance(email, str) and email.strip() != '':
            self.__email = email
        else:
            print(f'Rejected: {email!r} is not a valid email')

    def set_age(self, age):
        if isinstance(age, int) and not isinstance(age, bool) and 0 <= age <= 120:
            self.__age = age
        else:
            print(f'Rejected: {age!r} is not a valid age')

    def set_phoneNo(self, phoneNo):
        if isinstance(phoneNo, int) and not isinstance(phoneNo, bool) and phoneNo >= 0:
            self.__phoneNo = phoneNo
        else:
            print(f'Rejected: {phoneNo!r} is not a valid phone number')

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