#To check if it is a leap year or not
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

#To check how many days are there in a certain month of that year
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month - 1]
  
year = int(input("Please enter a year: ")) # Enter a year
month = int(input("Please enter a month: ")) # Enter a month
days = days_in_month(year, month)
print(days)

