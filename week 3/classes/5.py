class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, balance):
        depo_again = int(input("Deposit account again: "))
        self.balance = balance + depo_again
        print("Current balance on", name, "account is:", self.balance)

    def withdraw(self):
        cash_out = int(input("How much money to withdraw?: "))
        if  self.balance >= cash_out:
            self.balance = self.balance - cash_out
            print("Current balance on", name, "account is:", self.balance)
        else:
            print("Insufficient funds!")

name = input("Please enter you name: ")
his_shekels = int(input("How much do you want to deposit?: "))
print("Current balance on", name, "account is:", his_shekels)
user = Account(name, his_shekels)
user.deposit(his_shekels)
user.withdraw()