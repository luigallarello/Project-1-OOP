from account import Account

class EverydayAccount(Account):
    MAX_WITHDRAWAL = 1000

    def __init__(self, current_balance, account_number, account_holder_name):
        super().__init__(current_balance, account_number, account_holder_name)

    def get_account_type(self):
        return 'Everyday'

    def withdrawal(self, withdrawal_amt):
        if not self._validate_amount(withdrawal_amt, 'withdrawal'):
            return
        if withdrawal_amt > self.MAX_WITHDRAWAL:
            print(f'Rejected: withdrawal exceeds the maximum of '
                  f'${self.MAX_WITHDRAWAL} per transaction.')
        else:
            super().withdrawal(withdrawal_amt)
