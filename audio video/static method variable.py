class SavingsAccount:
    branch_name="ameerpet"
    branch_ifsc = "2000otst"
    @staticmethod
    def show():
        print(SavingsAccount.branch_name)
        print(SavingsAccount.branch_ifsc)
SavingsAccount.show()
