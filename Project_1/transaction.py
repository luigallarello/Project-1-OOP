class Transaction():

    def __init__(self, transaction_id, transaction_type, transaction_amt, transaction_desc, status="Pending"):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.transaction_amt = transaction_amt
        self.transaction_desc = transaction_desc
        self.status = status

    def __str__(self):
            return f'Transaction ID: {self.transaction_id}\n Transaction type: {self.transaction_type}\n Amount: {self.transaction_amt}\n Description: {self.desc}\n Current Status: {self.status}'
    
    def process_transaction(self, account):
        if self.transaction_type == "deposit":
            if self.transaction_amt < 0:
                    self.transaction_amt = int(input("Please enter a valid number:"))
            else:
                account.deposit(self.transaction_amt)
                self.status = "Processed"
        elif self.transaction_type == "withdrawl":
            account.withdrawl(self.transaction_amt)
            self.status = "Processed"

    def cancel_transaction(self):
            if self.status == "Pending":
                self.status = "Cancelled"
                print('Transaction is cancelled')
            elif self.status == "Processed":
                print("This transaction has already been processed.")

    def update_transaction(self):
            self.desc = input('Please update transaction description')








