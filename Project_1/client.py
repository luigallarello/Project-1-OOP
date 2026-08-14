class Client:
    def __init__(self, clientNo, firstName, lastName, email, age, phoneNo):
        self.clientNo = clientNo
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.age = age
        self.phoneNo = phoneNo
        
def __str__(self):
        return f'Current balance: {self.currentBalance}\n Account Type: {self.accountType} \n Account Number: {self.accountNumber}'
    def display_contact_info(self):
        print(f'''Client Number: {self.clientNo},\n 
            First Name: {self.firstName},\n
            Last Name: {self.lastName},\n
            Email: {self.email},\n
            Age: {self.age},\n
            Phone No: {self.phoneNo}''')