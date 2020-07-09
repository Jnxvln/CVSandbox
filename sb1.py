import datetime

def print_date():
  # datetime.date.today() returns in format YYYY-MM-DD   :(
  date = datetime.date.today()

  # convert to MM-DD-YYYY    :)
  return date.strftime('%m/%d/%Y')


def hi_daniel():
  return print(f"Hi Daniel! Today is {print_date()} and we'll make some cool shit in Python")


# Start program
hi_daniel()