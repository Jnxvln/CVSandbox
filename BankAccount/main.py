from Customer import Customer
from Account import Account, CHECKING, SAVINGS

def print_balance(account):
  print('Account Balance: ${}'.format(account.balance))
  return

# Create a Customer instance
customer1 = Customer('John', 'Doe', 42)
print('Created customer1 as John Doe, age 42')

# Create an Account instance
customer1.create_account(CHECKING, 100.00)
print('Created a checking account for John Doe')

# DEPOSIT MONEY

# get the account
c1_checking = customer1.get_checking()
print_balance(c1_checking)

# deposit money and return balance
print('Depositing $50.00')
print('Account Balance: ${}'.format(c1_checking.deposit(50.00)))

# WITHDRAW MONEY

# withdraw money from checking
print('Withdrawing $25.00 for gas')
gas_money = c1_checking.withdraw(25.00)
print('Gas money: $', gas_money)
print_balance(c1_checking)