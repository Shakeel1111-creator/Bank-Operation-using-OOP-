#Bank Operation Using OOP in Python


class bank:
    bankname="Union Bank Of India"
    branch='V.kota Chittoor'

    #Account Creation
    def __init__(self,username,pan,address):
        self.username=username
        self.pan=pan
        self.address=address
        self.balance=0.0
        print(f'\nCongratulations {self.username}! Your account created successfully')

    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f'\n{amount} amount is deposited into your account successfully')
        print(f'Your current balance is {self.balance}')

    def withdraw(self,amount):
        if(self.balance>amount):
            self.balance=self.balance-amount
            print(f'{amount} withdrawn successfully')
            print(f'Your current balance is {self.balance}')
        else:
            print("Insufficient Fund....")

    def ministatement(self):
        print(f'\n{self.username} your current balance is {self.balance}')

#user_input
print(f'Welcome to {bank.bankname} {bank.branch} ')
username=input("enter your name:")
pan=input("enter you pan-card no:")
address=input("enter your address:")

b1=bank(username,pan,address)

while True:
    print('\n1.Deposit\n2.WithDraw\n3.Mini Statement\n4.Stop')
    ch=int(input('\nEnter your choice:'))
    if ch==1:
        amount=float(input('\nenter the amount you want to deposit  :'))
        b1.deposit(amount)
    elif ch==2:
        amount=float(input('\nenter the amount you want to withdraw   :'))
        b1.withdraw(amount)
    elif ch==3:
        b1.ministatement()
    elif ch==4:
        print(f'\nThank you {b1.username} for using {bank.bankname}........')
        break
    else:
        print('\nInvalid choice please enter valid option:')
        
        

