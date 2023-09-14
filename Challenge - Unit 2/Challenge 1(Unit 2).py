class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def depositmoney(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposited ", amount, " New balance:", self.__account_balance)
    else:
      print("Invalid deposit amount. Please deposit a positive amount.")

  def withdrawmoney(self, amount):
    if 0 < amount <= self.__account_balance:
      self.__account_balance -= amount
      print("Withdraw ", amount, " New balance:", self.__account_balance)
    else:
      print("Invalid withdrawal amount or insufficient balance.")

  def accountbalance(self):
    print(f"Accountbalance for ", self.__account_holder_name, " Account ",
          self.__account_number, "is ", self.__account_balance)


name = input("name:")
accnum = input("acc_number:")
account1 = BankAccount(accnum, name, 5000)
print("press 1 for deposit")
print("press 2 for withdraw")
print("press 3 for check balance")
ch = int(input("enter your choice:"))
if (ch == 1):
  dep = int(input("Enter a amount to deposit:"))
  account1.depositmoney(dep)
elif ch == 2:
  wi = int(input("Enter a amount to withdraw:"))
  account1.withdrawmoney(wi)
elif ch == 3:
  print("your current balance is 5000.")
else:
  print("Invalid choice")
