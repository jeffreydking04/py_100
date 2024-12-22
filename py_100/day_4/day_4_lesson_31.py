# Python uses the Mersenne Twister as its pseuderandom generator
# Visit Kahn Academy for a simple explanation of random number generators

# Python Random Module

import random
import my_module
import math

# We are concerned with random.randint(a, b)  => random interger inclusive of a and b

random_integer = random.randint(1, 10)
print(random_integer) 

# MODULES!! reduce complexity and enable collaboration

print(my_module.my_favorite_number)

# random.random() is the best: numbers between 0 and 1 (direct relationship with probability)

random_number_0_to_1 = random.random()

print(random_number_0_to_1)

# I freaking love it

random_number_0_to_10 = random.random() * 10

print (random_number_0_to_10)

random_float = random.uniform(1, 10)

print(random_float)

# there may be some issues on the edge cases with random.uniform
# using random.random then multiplying to get your range is a sure bet and you don't have to remember any other functions!

# random number between 1 and 6:

dice_roll = math.floor(random.random() * 6) + 1

print(dice_roll)

for x in range(0,10):
    print(math.floor(random.random() * 6) + 1)

# Quick code challenge: print heads or tails based on rng.  Already did something similar above, but let's do it.

for x in range(0,10):
    random_even_odd = math.floor(random.random() * 2)
    print(random_even_odd)
    if random_even_odd == 0:
        print('Heads')
    else:
        print('Tails')

# We could have used randint(0, 1), but I like the above.

# Okay, so let's talk about the elephant in the directory. Using my_module (and running the code) created a __pycache__ sub directory.
# I might have to add this to the .gitignore
# Not going to pursue this right now; plowing ahead with the lesson. I should keep track of things I need to pursue later, though.
# I will pursue that tracking later. lol
