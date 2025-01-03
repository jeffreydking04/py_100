# Day 10 Lesson 76: Calculator Project

# What's on the screen: serves as pseudo code for easy projects

# Welcome

# What's the first number?
# Input num
# List of Operations
# Pick an operation
# Input op
# What's the next number
# Input num2
# Show calculation and answer eg 2 + 5 = 7
# Prompt to continue with value of the answer and new operation or new calc or quit
# Clear screen
# If continue, display previous value, go to pick operator
# If new, go to first number input
# If q, goodbye


import os

def clear_screen():
    os.system('clear')

ops = '+-*/'

# found this on stackoverflow, with around a billion other people; very nice
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def get_op():
    print('\n')
    for op in ops:
        print(op)
    valid = False
    while not valid:
        op = input('Pick an operation:\n\n')
        if op not in ops:
            print('Invalid Input.')
        else:
            valid = True
    return op

def get_num(order):
    valid_input = False
    while not valid_input:
        num = input(f'What is the {order} number?\n\n')
        if is_number(num):
            valid_input = True
        else:
            print('Invalid Input.')
    return float(num)

def perform_op(n1, n2, op):
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    return n1 / n2

def get_next_action():
    valid = False
    while not valid:
        action = input('Would you like to continue calculating with the result (y), start a new calculatio (n), or quit (q)?\n\n').lower()
        if action not in 'ynq':
            print('Invalid Input.')
        else:
            valid = True
    return action

def display_as_int_or_float(num):
    if int(num) == float(num):
        return int(num)
    return num

clear_screen()

print('Welcome to calculator.')

should_continue = True
skip_first_input = False
while should_continue:
    if not skip_first_input:
        num1 = get_num('first')
    skip_first_input = False
    op = get_op()
    num2 = get_num('second')
    answer = perform_op(num1, num2, op)
    print(f'{display_as_int_or_float(num1)} {op} {display_as_int_or_float(num2)} = {display_as_int_or_float(answer)}\n\n')
    next_action = get_next_action()
    if next_action == 'y':
        num1 = answer
        skip_first_input = True
        clear_screen()
        print(f'Calculating off previous result: {display_as_int_or_float(num1)}\n\n')
    elif next_action == 'n':
        clear_screen()
    else:
        should_continue = False

clear_screen()
print('Goodbye!\n\n')


# Instructor Yu used recursion to solve the multiple while issue that I solved with the skip.
