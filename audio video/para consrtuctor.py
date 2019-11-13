class SavingsAccount:
    def __init__(self,acno,name,bal):
        self.acno=acno
        self.name=name
        self.bal=bal
    def display(self):
        print("acno=",self.acno)
        print("name=",self.name)
        print("balance=",self.bal)
a=SavingsAccount(101,"ravi",15789.00)
a.display()