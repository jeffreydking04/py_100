# Day 8 Lesson 62: Positional vs keyword

# This was an actual lesson, not guiding through a solution, so documenting

def greet_with_name(name):
    print(f'Hello {name}.')
    print(f'How do you do, {name}?')

# Functions with more than one input
def greet_with(name, location):
    print(f'Hello {name}.')
    print(f'What is it like in {location}?')

# This is the common syntax using keyword:
greet_with(name='Arya', location='Winterfell')
greet_with(name='Winterfell', location='Arya')

# Positional:
greet_with('Arya', 'Winterfell')
