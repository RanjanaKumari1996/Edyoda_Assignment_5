class Account:

    def __init__(self,title,balance):
        
        self.title=title
        self.ac_balance=balance
    

    
class SavingsAccount(Account):

    def __init__(self,title,balance,interest_rate):
    
        super().__init__(title,balance)
    
        self.interestRate=interest_rate
    
    def display(self):
        print(self.title, "is the title", self.ac_balance, "is the balance", self.interestRate, "is the interestRate")
        print(end="\n")

print(end="\n")

Ac_name=input("Enter title of Account holder: ")
Ac_balnce=int(input("Enter account balance: "))
Interest_rt=int((input("Enter the interest rate: ")))
print(end="\n")

Saving_ac_obj=SavingsAccount(Ac_name,Ac_balnce,Interest_rt)
print(end="\n")

Saving_ac_obj.display()

