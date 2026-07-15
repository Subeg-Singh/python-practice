class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        self.balance-=amount

    def display_balance(self):
        print(f'balance is {self.balance}')

acc1 = BankAccount("Subeg", 5000)

def Info():
    ch=input('Enter 1 to display balance, 2 to deposit, 3 to withdraw:')
    if ch=='1':
        acc1.display_balance()
    elif ch=='2':
        depo=int(input('Enter amt to be deposited:'))
        acc1.deposit(depo)
        acc1.display_balance()
    elif ch=='3':
        withdr=int(input('Enter amt to be withdrawn:'))
        acc1.withdraw(withdr)
        if acc1.balance<0:
           print('insufficient balance')
        acc1.display_balance()
    else:
        print('INVALID CHOICE')

Info()

# next is to store the balance in a file and read it from there.