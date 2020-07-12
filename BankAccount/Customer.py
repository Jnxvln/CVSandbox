# This program simulates basic banking operations
from Account import Account, CHECKING, SAVINGS

class Customer():
  def __init__(self, fname, lname, age):
    self.first_name = fname
    self.last_name = lname
    self.age = age
    self.accounts = []

  @property
  def first_name(self):
    return self.__first_name

  @property
  def last_name(self):
    return self.__last_name

  @property
  def age(self):
    return self.__age


  @first_name.setter
  def first_name(self, fname):
    self.__first_name = fname

  @last_name.setter
  def last_name(self, lname):
    self.__last_name = lname

  @age.setter
  def age(self, age):
    self.__age = age

  def get_checking(self):
    for account in self.accounts:
      checking_accounts = []
      if account.brand == 'checking':
        checking_accounts.append(account)

      # For now, just return the first one (implent a primary checking class field later?)
      return checking_accounts[0]

  def create_account(self, account_type, starting_balance):
    # Check that account_type is either CHECKING or SAVINGS constant
    if account_type != CHECKING and account_type != SAVINGS:
      return ValueError('ERROR: New account type must be either "checking" or "savings" only')
    
    account = Account(account_type, starting_balance)
    self.accounts.append(account)

    print('{} created successfully!'.format(str(account)))

  def __str__(self):
    return '{} {}'.format(self.first_name, self.last_name)