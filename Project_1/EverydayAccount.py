from account import Account

class EverydayAccount(Account):
    def __init__(self, current_balance, account_number, account_holder_name, max_withdrawal_amt=1000):
        super().__init__(current_balance, account_number)
        self.__max_withdrawal_amt = max_withdrawal_amt

    def get_account_type(self):
        return 'Everyday'
    
    def _withdrawal(self, withdrawal_amt):
        if withdrawal_amt > self.__max_withdrawal_amt:
            print('Proposed amount is greater than your limit')
            return False
        else:
            super()._withdrawal(withdrawal_amt)
            return True