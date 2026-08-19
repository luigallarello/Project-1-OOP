class Transaction():

    def __init__(self, transaction_id, transaction_type, transaction_amt, transaction_desc, status="Pending"):
        self.__transaction_id = transaction_id
        self.__transaction_type = transaction_type
        self.__transaction_amt = transaction_amt
        self.transaction_desc = transaction_desc
        self.__status = status

    def get_transaction_id(self):
        return self.__transaction_id

    def get_transaction_type(self):
        return self.__transaction_type

    def get_transaction_amt(self):
        return self.__transaction_amt

    def set_transaction_id(self, transaction_id):
        if isinstance(transaction_id, int):
            self.__transaction_id = transaction_id

    def set_transaction_type(self, transaction_type):
        if isinstance(transaction_type, str):
            return self.__transaction_type

    def set_transaction_amt(self, transaction_amt):
        if isinstance(transaction_amt, (int, float)):
            return self.__transaction_amt

    def set_status(self, status):
        if isinstance(status, str):
            return self.__status

    def __str__(self):
        return f'Transaction ID: {self.__transaction_id}\n Transaction type: {self.__transaction_type}\n Amount: {self.__transaction_amt}\n Description: {self.desc}\n Current Status: {self.__status}'

    def __repr__(self):
        return f'Transaction(Transaction ID={self.__transaction_id!r}, Type={self.__transaction_type!r}, Amount={self.__transaction_amt!r}, Description={self.desc!r}, Status={self.__status!r})'

    def process_transaction(self, account):
        if self.__transaction_type == "deposit":
            if self.__transaction_amt < 0:
                    self.__transaction_amt = int(input("Please enter a valid number:"))
            else:
                account.deposit(self.__transaction_amt)
                self.__status = "Processed"
        elif self.__transaction_type == "withdrawl":
            account.withdrawl(self.__transaction_amt)
            self.__status = "Processed"

    def cancel_transaction(self):
        if self.__status == "Pending":
            self.__status = "Cancelled"
            print('Transaction is cancelled')
        elif self.__status == "Processed":
            print("This transaction has already been processed.")

    def update_transaction(self):
        self.desc = input('Please update transaction description')








