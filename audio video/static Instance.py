class SavingsAccount:
    branch_name="ameerpet"
    branch_ifsc = "0211ds01"
    def assign(self,acno,balance):
        self.acno=acno
        self.balance=balance
    def display(self):
        print("branch_name=",SavingsAccount.branch_name)
        print("branch_ifsc=", SavingsAccount.branch_ifsc)
        print("acno=",self.acno)
        print("balance=",self.balance)
a=SavingsAccount()
a.assign(1001,12900.00)
a.display()
b=SavingsAccount()
b.assign(1002,12900.00)
b.display()