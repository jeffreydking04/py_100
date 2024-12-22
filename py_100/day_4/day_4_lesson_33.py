# Code Challenge: Who will pay the bill?
# print a random name from the list

import math
import random

friends = ['Alice', 'Bob', 'Charlie', 'David', 'Emanuel']

for x in range(0,20):
    idx = math.floor(random.random() * len(friends))
    print(friends[idx])

# oooooh: random.choice(sequence)

for x in range(0,20):
    print(random.choice(friends))

# we also could hove used random.randint(0, 4)

for x in range(0,20):
    print(friends[random.randint(0,4)])
