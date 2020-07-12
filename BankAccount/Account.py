import uuid
from random import seed
from random import random

CHECKING = 'checking'
SAVINGS = 'savings'

class Account():
  def __init__(self, account_type, starting_balance):
    self.brand = account_type
    self.balance = starting_balance
    self.number = self.generate_account_number()

  @property
  def balance(self):
    return self._balance

  @property
  def brand(self):
    return self._brand

  @property
  def number(self):
    return self._number

  @balance.setter
  def balance(self, bal):
    self._balance = bal

  @brand.setter
  def brand(self, brand):
    self._brand = brand

  @number.setter
  def number(self, num):
    self._number = num

  def deposit(self, amt):
    self.balance += amt
    return self.balance

  def withdraw(self, amt):
    self.balance -= amt
    return amt

  def generate_account_number(self):
    rand_seed = uuid.uuid4()
    seed(rand_seed)
    number = random()
    number = int(number * 100000000000000)
    return number


  def __str__(self):
    return '{} account: {}'.format(str(self.brand), self.number)