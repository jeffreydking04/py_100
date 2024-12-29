# Day 8: Caesar Cipher Project

# The way Lessons 61 through 65 look structured, Instructor Yu is likely going 
# to lead us through another 'complicated' project instead of lecturing and then
# handing us the project, just like hangman.  I will likely just hit the project then watch the 
# videos and make notes and adjustments.

# 2 step imports 3
import os # almost always for terminal display, just keeps things tidy to clear screen between steps

# 3 step constants 4
messages = {
    'intro': 'Welcome to Caesar Cipher! Would you like to encode or decode?',
    'encode_prompt': 'Type the message you would like to encode:',
    'decode_prompt': 'Type the message you would like to decode:',
    'shift_prompt': 'Enter the shift amount:',
    'encode_result': 'Your encoded message:',
    'decode_result': 'Your decoded message:',
    'invalid_input': 'Invalid Input'
}

# 4 step state 4.5
state = {
    'mode': '', # 'encode' or 'decode' or 'q'
    'input': '',
    'output': '', # whether encoding or decoding, we are going to have a string input and a string output
    'message': 'intro',
    'invalid': False
}

def mode():
    return state['mode']

def user_input():
    return state['input']

def output():
    return state['output']

def set_mode(mode):
    state['mode'] = mode

def message():
    return state['message']

def set_message(message):
    state['message'] = message

def invalid():
    return state['invalid']

def set_invalid(invalid):
    state['invalid'] = invalid

def set_input(input):
    state['input'] = input

def set_output(output):
    state['output'] = output

def display_message():
    input(f'{messages[message()]}\n\n')

def valid_mode():
    if input() in ['encode', 'decode', 'q']:
        return True
    return False

# 4.5 step display 5
    # I knew I should be spacing out my node numbers as a best practice
while mode() != 'q':
    os.system('clear')
    if invalid():
        print(messages['invalid_input'])
        set_invalid(False)
    user_response = display_message()

# 5 step input_encode_decode 6
    if message() == 'intro':
        print('Here')
        if not valid_mode():
            set_invalid(True)
            continue
        if mode() == 'q':
            print('Goodbye!\n\n')
            break
        if mode() == 'encode':
            set_message('encode_prompt')
            continue
        set_message('decode_prompt')
        continue
        
    set_mode('q')

# 7 split is_5_valid 8 9

# 8 step 5_valid 10

# 9 step 5_invalid 5

# 10 step input_message 11

# 11 split is_10_valid 12 13

# 12 step 10_valid 14

# 13 step 10_invalid 10

# 14 step input_shift 15

# 15 split is_14_valid 16 17

# 16 step 14_valid 18

# 17 step 14_invalid 14

# 18 split e_or_d 19 20

# 19 step encode 21

# 20 step decode 22

# 21 end display_e 0

# 22 end display_d 0

