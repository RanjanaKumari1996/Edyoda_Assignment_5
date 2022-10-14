class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance-=amount

    def deposit(self, amount):
        self.balance+=amount

    def getBalance(self):
        return self.balance

class SavingsAccount(Account):

    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):

        self.interest_amount=self.interestRate*self.balance/100
        return self.interest_amount


print(end="\n")

Ac_name=input("Enter title of Account holder: ")
Ac_balnce=int(input("Enter account balance: "))
Interest_rt=int((input("Enter the interest rate: ")))
print(end="\n")

Saving_ac_obj=SavingsAccount(Ac_name,Ac_balnce,Interest_rt)
print(end="\n")

withdrawal_amount=int(input("Enter amount to be withdraw: "))

Saving_ac_obj.withdrawal(withdrawal_amount)
print("Account balance after withdrawal: ", Saving_ac_obj.getBalance())

deposit_amount=int(input("Enter amount to be deposit: "))

Saving_ac_obj.deposit(deposit_amount)
print("Account balance after deposit: ",Saving_ac_obj.getBalance())
print(end="\n")

print("Interest amount of current balance: ",Saving_ac_obj.interestAmount())