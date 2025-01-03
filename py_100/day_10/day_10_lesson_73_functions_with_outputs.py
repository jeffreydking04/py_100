# Day 10 Lesson 73: Functions with Outputs

import os

def clear_screen():
    os.system('clear')

clear_screen()

def format_name(first_name, last_name):
    # both are fine, of course
    # return f'{first_name.capitalize()} {last_name.capitalize()}'
    return f'{first_name} {last_name}'.title()
    # return is special
    # return('hi')
    # return 'hi'
    # both work
    # but, for example, print 'hi' does not work, it must be print('hi')

print(format_name('jeff', 'king'))

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_1('hello')
print(output)

output_2 = function_2(output)
print(output_2)
