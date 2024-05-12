try:
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))
except ValueError:
  print("Error: Please enter only numbers.")

print("You entered:", num1, "and", num2)
