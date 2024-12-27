# NOTE:  I have gone through this problem many, many times over the last few days, but that is because I have been 
# really focusing on using pseudo code and flow charts to dev.  This time through was just with psuedo code and 
# because the pseudo code was well formed, even though I had some moments where I was like what because
# Python syntax is still not engrained, I never ever had to figure out 'where' I was in the code  I knew
# exactly where I was and what was next even though I had occassionally scroll back up to change some implementation details

# Lesson 54: Picking a Random Word and Checking Answers (going to combine these in one file, this is just a way to show how we can use the pseudo code to construct)

# Using to dos: a great idea.  Can use our pseudo code syntax:

# Remember the syntax here is: 
# flow chart node id, type of action (which we only have 4 of right now: start, end, step, split (decision)), easy identifier, what node(s) come next

# 1 start imports 2

# We are importing os to clear the screen between guesses for a cleaner interface.

import os
import random
import hangman_words
from hangman_art import hangman_images


# 2 step constants 3

# Boo, I thought we would import some wonderful library to get random words; we just made the list ourselves

def get_random_word():
    return random.choice(hangman_words.word_list)

alphabet = 'abcdefghijklmnopqrstuvwxyz'

messages = {
    'intro': 'Welcome!',
    'invalid': 'Invalid Input',
    'used': 'Already guessed that letter.',
    'correct': 'You chose wisely!',
    'incorrect': 'You chose poorly!',
    'won': 'You won!',
    'lost': 'You lost!'
}

chosen_word = get_random_word()
print(chosen_word)

# 3 step state 4

# We wrap state in a dictionary so any functions that get state won't get a stale copy

state = {
    'user_guess': '',
    'available': alphabet,
    'misses': 0,
    'correct_guesses': '',
    'message': 'intro'
}

# 4 step display 5

def word_found():
    word_found = True
    for letter in chosen_word:
        if letter not in state['correct_guesses']:
            word_found = False
    return word_found

def display_word():
    str = ''
    for letter in chosen_word:
        if letter in state['correct_guesses']:
            str += letter + ' '
        else:
            str += '_ '
    return str

def display_image():
    print(hangman_images[state['misses']], '\n\n')

def display_message():
    if state['message'] != 'intro':
        print('Last guess:', state['user_guess'], '\n\n')
    print(messages[state['message']], '\n\n')

while not word_found() and state['misses'] < len(hangman_images) - 1:
    os.system('clear')
    display_image()
    print(state['available'], '\n\n')
    print(display_word(), '\n\n')
    print('Lives Left:', 6 - state['misses'], '\n\n')
    display_message()

    # 5 step input 6

    user_guess = state['user_guess'] = input('What is your guess? \n\n').lower()
    
    # 6 split is_valid 7 8

    if user_guess not in alphabet:
        # 7 step invalid 1
        # set the message to invalid choice and restart the loop
        state['message'] = 'invalid'
        continue

    # 8 step valid 9 
    # if we got here and it must be a valid letter
    
    # 9 split is_available 10 11
    if user_guess not in state['available']:
        # 10 step unavailable 1
        # set message and restart loop
        state['message'] = 'used'
        continue

    # 11 step available 12
    # if we are here it must be available, but now it has been chose, so remove it
    state['available'] = state['available'].replace(user_guess, '')

    # 12 split is_correct 13 14
    if user_guess in chosen_word:
        # 13 step correct 15
        state['correct_guesses'] += user_guess

        # 15 split won_game 16 17
        if word_found():
            # 16 end won 0
            os.system('clear')
            display_image()
            state['message'] = 'won'
            print('The word was', chosen_word, '\n\n')
            display_message()

        # 17 step did_not_win 1

        else:
            state['message'] = 'correct'

# 14 step incorrect 18

    else:
        state['misses'] += 1
        # 18 split lost_game 19 20
        if state['misses'] >= len(hangman_images) - 1:
            # 19 end lost 0
            os.system('clear')
            state['message'] = 'lost'
            display_image()
            print('The word was', chosen_word, '\n\n')
            display_message()

        else:
            # 20 step did_not_lose 1
            state['message'] = 'incorrect'
