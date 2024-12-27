import os

images = [
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

alphabet = 'abcdefghijklmnopqrstuvwxyz'

messages = {
    'intro': 'Welcome to Hangman!',
    'invalid': 'Invalid Input!',
    'previous': 'You already used that letter!',
    'incorrect': 'You chose poorly!',
    'correct': 'You chose wisely!',
    'winner': 'You won!',
    'loser': 'You have been hanged!'
}

def get_word():
    return 'hangman'

word = get_word()

game_state = {
    'user_guess': '',
    'correct_answers': '',
    'available': alphabet,
    'selected_message': 'intro',
    'misses': 0,
}

def user_guess():
    return game_state['user_guess']

def correct_answers():
    return game_state['correct_answers']

def available():
    return game_state['available']

def selected_message():
    return game_state['selected_message']

def set_user_guess(val):
    game_state['user_guess'] = val

def add_to_correct_answers(val):
    game_state['correct_answers'] += val

def remove_from_available(val):
    game_state['available'] = game_state['available'].replace(val, '')

def set_selected_message(val):
    game_state['selected_message'] = val 

def misses():
    return game_state['misses']

def increment_misses():
    game_state['misses'] += 1

def word_found():
    word_found = True
    for letter in word:
        if letter not in correct_answers():
            word_found = False
    return word_found

while not word_found() and misses() < 6:
    os.system('clear')
    print(images[misses()], '\n')
    print(available(), '\n')
    display_str = ''
    for letter in word:
        if letter in correct_answers():
            display_str += letter + ' '
        else:
            display_str += '_ '
    print(display_str, '\n')
    if user_guess():
        print('Previous Choice:', user_guess(), '\n')
    print(messages[selected_message()], '\n')
    set_user_guess(input('Enter your guess:\n\n').lower())
    if user_guess() in alphabet and user_guess():
        if user_guess() in available():
            remove_from_available(user_guess())
            if user_guess() in word:
                set_selected_message('correct')
                add_to_correct_answers(user_guess())
                if word_found():
                    os.system('clear')
                    print(images[misses()], '\n')
                    print('The word was:', word, '\n')
                    print('You Win!\n')
            else:
                increment_misses()
                set_selected_message('incorrect')
                if misses() == 6:
                    os.system('clear')
                    print(images[misses()], '\n')
                    print('The word was:', word, '\n')
                    print('You have been hanged!\n')
        else:
            set_selected_message('previous')
    else:
        set_selected_message('invalid')
