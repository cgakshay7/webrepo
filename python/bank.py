class Bankaccount:
    def __init__(self,accname,accnum,acctype,balance):
        self.accname=accname
        self.accnum=accnum
        self.acctype=acctype
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print("Deposit successfull of :",amount)
            print("New balance is :",self.balance)
        else:
            print("invalid amount")

    def withdraw(self,amount):
        if 0<amount<self.balance:
            self.balance=self.balance-amount
        elif amount>self.balance:
            print("not possible to withdaw")
        else:
            print("invalid")

    def getbalance(self):
        print("current balance :",self.balance)
ano=int(input("enter the account number"))
name=input("enter account name")
atype=input("enter account type")
amt=int(input("enter current balance"))
account1=Bankaccount(ano,name,atype,amt)
account1.getbalance()
ch=0
while(ch!=4):
      print("\n1.Deposit amount\n2.Withdraw amount\n3.See account balance\n4.Exit")
      ch=int(input("enter the choice"))
      if ch==1:
          damount=int(input("enter the deposit amount"))
          account1.deposit(damount)
      elif ch==2:
          wamount=int(input("enter the withdrawal amount"))
          account1.withdraw(wamount)
      elif ch==3:
          account1.getbalance()
      else:
          print("invalid")