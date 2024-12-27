import os

# Setup

# List
def construct_list_of_hangman_images():
    return [
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

# List
def construct_letter_choices():
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Dictionary
def construct_possible_responses_to_input():
    return {
        'intro': 'Welcome to Hangman!',
        'incorrect_choice': 'You chose poorly!',
        'correct_choice': 'You chose wisely!',
        'previously_used': 'You have guessed that previously!',
        'invalid_response': 'Invalid Input!'
    }

# String
def get_random_word():
    return 'hangman'

game_state = {
    'images': construct_list_of_hangman_images(),
    'alphabet': construct_letter_choices(),
    'available': construct_letter_choices(),
    'response_messages': construct_possible_responses_to_input(),
    'response_choice': 'intro',
    'correct_guesses': [],
    'word_to_guess': get_random_word(),
    'user_guess': '',
    'incorrect_guesses_left': 6
}

# Functions

# String
def word_to_guess():
    return game_state['word_to_guess']

# List
def correct_guesses():
    return game_state['correct_guesses']

# String
def user_guess():
    return game_state['user_guess']

# List
def alphabet():
    return game_state['alphabet']

# List
def available():
    return game_state['available']

# Integer
def incorrect_guesses_left():
    return game_state['incorrect_guesses_left']

# List
def response_choice():
    return game_state['response_choice']

# Dictionary
def response_messages():
    return game_state['response_messages']

# List
def images():
    return game_state['images']

# Void
def display_losing_message():
    os.system('clear')
    display_image()
    print('HUNG!\n')
    print('The word was', word_to_guess() + '!\n')

# Void
def display_winning_output():
    os.system('clear')
    display_image()
    print('The word was', word_to_guess() + '!\n')
    print('You Win!\n')

# Void
def display_invalid_response_message():
    print('Invalid Input')

# Boolean
def check_for_win():
    is_winner = True
    for letter in word_to_guess():
        if letter not in correct_guesses():
            is_winner = False
    return is_winner

# Void
def update_correct_guesses():
    correct_guesses().append(user_guess())

# Boolean
def is_valid_input():
    return user_guess() in alphabet()

# Void
def get_user_guess():
    game_state['user_guess'] = input('Enter your guess:\n\n').lower()

# Void
def display_response_message():
    print(response_messages()[response_choice()], '\n')

# Void
def display_word_state():
    display_string = ''
    for letter in word_to_guess():
        if letter in correct_guesses():
            display_string += letter
        else:
            display_string += '_'
        display_string += ' '
    print(display_string, '\n')

# Void
def display_available():
    print(available(), '\n')

# Void
def display_previous_choice():
    print('Previous Choice:', user_guess(), '\n')

# Void
def display_image():
    print(images()[6 - incorrect_guesses_left()])

# Void
def remove_choice_from_available():
    available().remove(user_guess())

# Boolean
def is_unused_choice():
    return user_guess() in available()

# Boolean
def check_choice_in_word():
    return user_guess() in word_to_guess()

# Void
def set_response_choice(str):
    game_state['response_choice'] = str

# Void
def decrement_incorrect_guesses_left():
    game_state['incorrect_guesses_left'] -= 1

# Paths

# Path Seven
def handle_incorrect_choice():
    if incorrect_guesses_left() > 0:
        set_response_choice('incorrect_choice')
        display_state_and_get_input()
    else:
        display_losing_message()

# Path Six
def handle_correct_choice():
    set_response_choice('correct_choice')
    update_correct_guesses()
    word_found = check_for_win()
    if word_found:
        display_winning_output()
    else:
        display_state_and_get_input()

# Path Five
def display_previously_used_message():
    set_response_choice('previously_used')
    display_state_and_get_input()

# Path Four
def check_for_correct_choice():
    is_correct_choice = check_choice_in_word()
    if is_correct_choice:
        handle_correct_choice()
    else:
        decrement_incorrect_guesses_left()
        handle_incorrect_choice()

# Path Three
def display_invalid_response_message():
    set_response_choice('invalid_response')
    display_state_and_get_input()

# Path Two
def check_previously_used():
    choice_is_new = is_unused_choice()
    if choice_is_new:
        remove_choice_from_available()
        check_for_correct_choice()
    else:
        display_previously_used_message()

# Path One
def display_state_and_get_input():
    os.system('clear')
    display_image()
    display_available()
    display_word_state()
    display_previous_choice()
    display_response_message()
    get_user_guess()
    if is_valid_input():
        check_previously_used()
    else:
        display_invalid_response_message()

# Start Path One
display_state_and_get_input()
