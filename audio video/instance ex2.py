class SavingsAccount:
    def assign(self,ac,bal):
        self.acno=ac
        self.bala=bal
    def display(self):
            print("acno=",self.acno)
            print("balance=", self.bala)
a=SavingsAccount()
a.assign(101,124568.00)
a.display()
b=SavingsAccount()
b.assign(102,12458778.00)
b.display()

