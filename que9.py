import random

random_number = random.randint(1, 100)

with open("random_numbers.txt", "a") as file:
  file.write(str(random_number))

print(f"Generated random number: {random_number}")
print(f"Saved to file: random_numbers.txt")
