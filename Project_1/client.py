class Client:
    def __init__(self, clientNo, firstName, lastName, email, age, phoneNo):
        self.clientNo = clientNo
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.age = age
        self.phoneNo = phoneNo
        
    def __str__(self):
        return f'Client Number: {self.clientNo}\n Client Name: {self.firstName}{self.lastName}\n Phone Number: {self.phoneNo}'

    def __repr__(self):
        return f'Client(client number={self.clientNo!r}, first name={self.firstName!r}, last name={self.lastName!r}, email={self.email!r}, age={self.age!r}, phone number={self.phoneNo!r})'

    def display_contact_info(self):
        print(f'''Client Number: {self.clientNo},\n 
            First Name: {self.firstName},\n
            Last Name: {self.lastName},\n
            Email: {self.email},\n
            Age: {self.age},\n
            Phone No: {self.phoneNo}''')