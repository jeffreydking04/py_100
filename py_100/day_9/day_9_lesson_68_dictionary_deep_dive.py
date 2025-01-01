# Day 8 Lesson 68: Dictionary: Deep Dive

# Key/Values
# Nice, you can add a comma at the end of every k/v 
programming_dictionary = {
    'Bug': 'An error in a program that prevents the program from running as expected.',
    'Function': 'A piece of code that you can easily call over and over again.',
}

print(programming_dictionary['Bug'])

# Typos in referencing the key result in a KeyError

programming_dictionary['Loop'] = 'The action of doing something over and over again.'

empty_dictionary = {}

# Wipe an existing dictionary:

# programming_dictionary = {}

# Really just replacing one dictionary with an empty one

# Edit an item in a dictionary
programming_dictionary['Bug'] = 'A moth in your computer.'

# Loop through a dictionary
for thing in programming_dictionary:
    print(thing)

# So we are looping over the keys with that:

for key in programming_dictionary:
    print(key)

for key in programming_dictionary:
    print(programming_dictionary[key])

# She didn't cover this:
for value in programming_dictionary.values():
    print(value)

# Or this:
for key, value in programming_dictionary.items():
    print(key, value)

# Or other stuff:
a = ('One', 'Two')
d = { x: x + ' Way' for x in a if x != 'Two'}
print(d)

# I am not really grousing, but I was actually hoping for a deep dive.
