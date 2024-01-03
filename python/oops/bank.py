class BankAccount:
    def __init__(self, acc_num, acc_holder_name, acc_type, balance=0):
        self.acc_num = acc_num
        self.acc_holder_name = acc_holder_name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit of ${amount} successful. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount. Please enter a positive value."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal of ${amount} successful. New balance: ${self.balance}"
        elif amount > self.balance:
            return "Insufficient funds. Withdrawal unsuccessful"
        else:
            return "Invalid withdrawal amount. Please enter a positive value."

    def get_balance(self):
        return f"Current balance: ${self.balance}"

print("Enter Details:")
ac_no = int(input("\nEnter account number: "))
name = input("\nEnter your name: ")
acc_type = input("\nEnter account type:")
amt = float(input("\nEnter amount:"))
s1 = BankAccount(ac_no, name, acc_type, amt)

deposit_amount = float(input("\nEnter deposit amount: "))
print(s1.deposit(deposit_amount))

withdraw_amount = float(input("\nEnter withdrawal amount: "))
print(s1.withdraw(withdraw_amount))
