# Lesson 41: Project: Create a Password Generator

#Password Generator Project
import random
import math
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_password = ''
# I figured using random.choice() would be cheating.
for n in range(0, nr_letters):
    i = math.floor(random.random() * len(letters))
    new_char = letters[i]
    easy_password += new_char

for n in range(0, nr_symbols):
    i = math.floor(random.random() * len(symbols))
    new_char = symbols[i]
    easy_password += new_char

for n in range(0, nr_numbers):
    i = math.floor(random.random() * len(numbers))
    new_char = numbers[i]
    easy_password += new_char

print(easy_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_length = len(easy_password)
hard_password = ''

for n in range(0, password_length):
    i = math.floor(random.random() * len(easy_password))
    new_char = easy_password[i]
    hard_password +=  new_char
    easy_password = easy_password[:i] + easy_password[i + 1:]

print(hard_password)
