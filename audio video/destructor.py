class Savingsaccount:
    def __init__(self):
        print("im a constuctor")
    def show(self):
        print("iam instance method")
    def __del__(self):
        print("i am a destructor")
a=Savingsaccount()
a.show()
del a