# Project: Rock, Paper, Scissors

import rps_ascii_art
import random
import math

# get input from user

user_selection = int(input('Choose: Rock (0), Paper(1), Scissors(2)\n'))

if user_selection not in [0, 1, 2]:
    print('Invalid entry!')
    quit()

random_computer_selection = math.floor(random.random() * 3)

result = user_selection - random_computer_selection

print('Your selection:')
print(rps_ascii_art.acscii[(int(user_selection))])
print('Computer selection')
print(rps_ascii_art.acscii[(int(random_computer_selection))])

if result == 0:
    print("It's a draw!")
elif result == 1 or result == -2:
    print('You win!')
else:
    print('You lost!') 
