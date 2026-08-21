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

Workshop 3.1 19/08
This workshop had us making each of the variables become private. This is done using a double underscore for each variable that needs to be private. In the code review, the tutor I suggested that an integer can be assigned to an account number to ensure fairness which is something to note. I didn't get around to task 4 onwards so I'm completing that on 21/08.

Workshop 3.2 21/08
This workshop I am finishing up what I missed out on in the earlier workshop. This includes the first uml, and then coding relationships between classes.