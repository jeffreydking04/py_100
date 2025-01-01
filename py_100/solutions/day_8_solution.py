# Day 8: Project: Caesar Cypher

import os

small_letters = 'abcdefghijklmnopqrstuvwxyz'
large_letters = small_letters.upper()

state = {
    'user_input': ''
}

def user_input():
    return state['user_input']

def set_user_input(val):
    state['user_input'] = val

def shift_letter(l, shift):
    if l in small_letters:
        idx = (small_letters.index(l) + shift) % 26
        return small_letters[idx]
    
    idx = (large_letters.index(l) + shift)
    idx %= 26
    return large_letters[idx]

def encode_message(shift):
    shifted_message = ''
    for l in user_input():
        if l != ' ':
            shifted_message += shift_letter(l, int(shift))
        else:
            shifted_message += ' '
    return shifted_message

def print_invalid_input():
    os.system('clear')
    print('Invalid Input!')

def get_shift():
    return input('What shift?\n\n')

os.system('clear')
 
print('Welcome to Caesar Cipher!')

while not user_input() == 'q':
    set_user_input(input('Would you like to encode, decode, or q?\n\n').lower())
    if user_input() not in ['encode', 'decode', 'q']:
        print_invalid_input()
        continue
    if user_input() == 'q':
        os.system('clear')
        print('Goodbye!\n\n')
        continue
    mode = user_input()
    set_user_input(input(f'Enter message to {user_input()}:\n\n'))
    while not user_input().isalpha():
        print_invalid_input()
        set_user_input(input(f'Enter message to {user_input()}:\n\n'))
    shift = get_shift()
    while not shift.isnumeric():
        print_invalid_input()
        shift = get_shift()
    print(f'The {mode}d message is:', encode_message(shift if mode == 'encode' else -int(shift)))
    input('Enter any key to continue: \n\n')
    os.system('clear')
