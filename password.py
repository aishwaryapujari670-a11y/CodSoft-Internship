# TASK 3 - PASSWORD GENERATOR

import random
import string

print("--- PASSWORD GENERATOR ---")

length = int(input("Enter password length (example 8, 12): "))

letters = string.ascii_letters  # A-Z, a-z
numbers = string.digits         # 0-9
symbols = string.punctuation    # !@#$ etc

all_chars = letters + numbers + symbols

password = ""
for i in range(length):
    password = password + random.choice(all_chars)

print(f"Your Strong Password is: {password}")
print("Copy and save it safely!")