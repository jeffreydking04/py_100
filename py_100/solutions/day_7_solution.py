# Day 7: Project: Hangman

import os

hangman_images = [
    '''
           _______
     |/      |
     |   
     |     
     |       
     |      
     |
    _|___
    ''',
    '''
           _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___
    ''',
    '''
           _______
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
    _|___
    ''',
    '''
           _______
     |/      |
     |      (_)
     |      \|
     |       |
     |      
     |
    _|___
    ''',
    '''
           _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___
    ''',
    '''
           _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___
    ''',
    '''
           _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___
    '''
]

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
available = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_random_word():
    return 'hangman'

random_word = get_random_word()
word_length = len(random_word)
display_word = '_ ' * word_length
word_state = '_' * word_length
misses = 0
word_found = False

# Yes, I know some people think it is a bad idea to create one line functions
# in anticipation of potential future complexity of that step, but I think it makes 
# the main loop far more readable provided function names are well thought out.
# You read the main code and you know exactly what it is doing based on english.
# You don't have to look up syntax you may not have encountered in the case of someone who
# is reading the code for an overview or for yourself if you are coming back to it later.
# You might trust that you implemented the function correctly and are just checking the 
# overall logic.  If you are anticipating more complex implementation, you have already abstracted
# the function.  This is the case here.  Many of these displays

def print_hangman_image(misses):
    print(hangman_images[misses], '\n')

def display_word_state():
    print('Word to guess:', display_word, '\n')

def display_available_letters():
    print('Available Letters', available, '\n')

def prompt_user():
    return input('What is your guess?\n')

def is_valid_char(char):
    return char.lower() in alphabet

def display_invalid_input():
    print('Invalid input')

def is_letter_already_chosen(char):
    return char in available

def display_letter_already_chosen():
    print('You have already guessed that letter.')

def remove_guess_from_available(char):
    available.remove(char)

def display_lost_message():
    print('HUNG!')
    print('The word was: ', random_word)

def is_letter_in_word(char):
    return char in random_word

def update_word_state(char, word_state, display_word):
    unfound_instances = random_word
    idx = unfound_instances.find(char)
    while idx > -1:
        word_state = word_state[:idx] + char + word_state[idx + 1:]
        idx_of_display_word = idx * 2
        display_word = display_word[:idx_of_display_word] + char + display_word[idx_of_display_word + 1:]
        unfound_instances = unfound_instances[:idx] + ' ' + unfound_instances[idx + 1:]
        idx = unfound_instances.find(char)
    return [word_state, display_word]

def display_correct_guess_message():
    print('Letter found!')

def display_incorrect_guess_message():
    print('You chose poorly!')

os.system('clear')
while not word_found and misses < 6:
    print_hangman_image(misses)
    display_word_state()
    display_available_letters()

    user_guess = prompt_user().lower()

    os.system('clear')
    if not is_valid_char(user_guess):
        display_invalid_input()
        continue

    if not is_letter_already_chosen(user_guess):
        display_letter_already_chosen()
        continue

    remove_guess_from_available(user_guess)

    if is_letter_in_word(user_guess):
        word_state, display_word = update_word_state(user_guess, word_state, display_word)
        display_correct_guess_message()
        if word_state == random_word:
            print('You won!\n The word was:', random_word)
            word_found = True
        continue

    # Incorrect guess block
    display_incorrect_guess_message()
    misses += 1
    if misses == 6:
        print_hangman_image(misses)
        display_lost_message()
