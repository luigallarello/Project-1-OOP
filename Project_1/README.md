Workshop 2.1, 12/08
In this workshop, we created the transaction and branch classes. At first, I struggled to understand the logic for the transaction at first but
then realised that it would be handling deposits and withdrawl. Our tutor explained it as the account methods could be adopted when the classes are imported into 
main.py. After that explanation I fully understood what the goal was.

    def cancel_transaction(self):
            if self.status == "Pending":
                self.status = "Cancelled"
                print('Transaction is cancelled')
            elif self.status == "Processed":
                print("This transaction has already been processed.")

The above piece of code is my cancel transaction method. Upon tutors review, there was no condition for if a transaction is alreadt cancelled it can't
go through. I still am yet to add this in but to do it, I will just create a third elif and say if the status is already cancelled then don't change the
status.