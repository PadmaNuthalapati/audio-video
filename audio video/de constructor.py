class SavingsAccount:
    def __init__(self):
        self.acno=101
        self.name="ravi"
        self.bal=123290.00
    def display(self):
        print("acno=",self.acno)
        print("name=", self.name)
        print("balance=", self.bal)
a=SavingsAccount()
a.display()