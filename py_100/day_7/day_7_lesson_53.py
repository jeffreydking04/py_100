# Lesson 53: How to break a complex problem down into a Flow Chart

# This lesson was about constructing a flow chart, which I got about 2 minutes into before getting really frustrated with how long
# it was taking to construct one.  Don't like my tools.  I want to be able to do it with text.  I envision psuedo code conversion, like so:


# images: List = construct_list_of_hangman_images()
# alphabet: List = construct_letter_choices()
# available: List = construct_list_of_unused_choices()
# response_messages: Dictionary = construct_possible_responses_to_input()
# response_choice: State = 'open'
# correct_guesses: List = construct_correct_guesses()
# word_to_guess: String = get_random_word()
# user_guess: State = ''
# incorrect_guesses_left: State = 6
# os.system('clear')
# path_one_display_state_and_get_input()
        
# path_one_display_state_and_get_input():
    # display_image()
    # display_available()
    # display_word_state()
    # display_response_message(response_choice)
    # user_guess: String = get_user_guess()
    # valid_response: Boolean = is_valid_input()
    # if valid_response:
        # path_two_check_previously_used()
    # else
        # path_three_display_invalid_response_message()

# path_two_check_previously_used():
    # choice_is_new: Boolean = is_unused_choice()
    # if choice_is_new:
        # remove_choice_from_available()
        # path_four_check_for_correct_choice()
    # else:
        # path_five_display_previously_used_message()

# path_three_display_invalid_response_message():
    # response_choice = 'invalid_response'
    # path_one_display_state_and_get_input()

# path_four_check_for_correct_choice():
    # is_correct_choice: Boolean = check_choice()
    # if is_correct_choice:
        # path_six_handle_correct_choice()
    # else:
        # incorrect_guesses_left -= 1
        # path_seven_handle_incorrect_choice()

# path_five_display_previously_used_message():
    # response_choice = 'previously_used'
    # path_one_display_state_and_get_input()

# path_six_handle_correct_choice():
    # response_choice = 'correct_choice'
    # update_correct_guesses()
    # word_found: Boolean = check_for_win()
    # if word_found:
        # display_winning_output()
    # else:
        # path_one_display_state_and_get_input()

# path_seven_handle_incorrect_choice():
    # if incorrect_guesses_left > 0:
        # response_choice = 'incorrect'
        # path_one_display_state_and_get_input()
    # else:
        # display_losing_message()


# Running the above through a code converter would work through the code backwards and return this:

# Would first check for libraries used and import at the top:

import os

# Setup

# List
def construct_list_of_hangman_images():
    return []

# List
def construct_letter_choices():
    return []

# List
def construct_list_of_unused_choices():
    return []

# Dictionary
def construct_possible_responses_to_input():
    return {}

# List
def construct_correct_guesses():
    return []

# String
def get_random_word():
    return ''

images = construct_list_of_hangman_images()
alphabet = construct_letter_choices()
available = construct_list_of_unused_choices()
response_messages = construct_possible_responses_to_input()
response_choice = 'open'
correct_guesses = construct_correct_guesses()
word_to_guess = get_random_word()
user_guess = ''
incorrect_guesses_left = 6
os.system('clear')

# Functions

# Void
def display_losing_message():
    pass

# Void
def display_winning_output():
    pass

# Void
def display_invalid_response_message():
    pass

# Boolean
def check_for_win():
    return True

# Void
def update_correct_guesses():
    pass

# Boolean
def is_valid_input():
    return True

# String
def get_user_guess():
    return ''

# Void
def display_response_message():
    pass

# Void
def display_word_state():
    pass

# Void
def display_available():
    pass

# Void
def display_image():
    pass

# Void
def remove_choice_from_available():
    pass

# Boolean
def is_unused_choice():
    return True

# Boolean
def check_choice():
    return True

# Paths

# Path Seven
def handle_incorrect_choice():
    if incorrect_guesses_left > 0:
        response_choice = 'incorrect'
        display_state_and_get_input()
    else:
        display_losing_message()

# Path Six
def handle_correct_choice():
    response_choice = 'correct_choice'
    update_correct_guesses()
    word_found = check_for_win()
    if word_found:
        display_winning_output()
    else:
        display_state_and_get_input()

# Path Five
def display_previously_used_message():
    response_choice = 'previously_used'
    display_state_and_get_input()

# Path Four
def check_for_correct_choice():
    is_correct_choice = check_choice()
    if is_correct_choice:
        handle_correct_choice()
    else:
        incorrect_guesses_left -= 1
        handle_incorrect_choice()

# Path Three
def display_invalid_response_message():
    response_choice = 'invalid_response'
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
    display_image()
    display_available()
    display_word_state()
    display_response_message()
    user_guess = get_user_guess()
    valid_response = is_valid_input()
    if valid_response:
        check_previously_used()
    else:
        display_invalid_response_message()

# Start Path One
display_state_and_get_input()
