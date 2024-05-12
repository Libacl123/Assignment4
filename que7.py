from datetime import date

birth_date = date(year=2000, month=12, day=29)  

# Get today's date
today = date.today()

# Calculate 
age = today.year - birth_date.year

# Checking
if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
  # If not, subtract 1 from age to account for incomplete year
  age -= 1

print(f"My age is: {age}")
