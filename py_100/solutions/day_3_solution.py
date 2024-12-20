# Day 3 Project: Treasure Island

print('Welcome to Treasure Island')

print('Your mission is to find the treasure.')

selected_direction = input('Would you like to go left or right?\n')

if selected_direction.lower() != 'left':
    print('You chose unwisely. Game Over.')
else:
    selected_travel_option = input('You come to a lake. '
                                   'There is an island in the middle of the lake. '
                                   'Would you like to swim or wait for a boat?\n')
    if selected_travel_option.lower() != 'wait':
        print('The boat you should have waited for ran you down. Game Over.')
    else: 
        selected_door_color = input('You have come to a building with three doors colored red, yellow, and blue. '
                                    'Which door would you like to open?\n').lower()
        if selected_door_color == 'yellow':
            print('You Win!')
        elif selected_door_color == 'red':
            print('You have stepped into a black hole. Game Over.')
        elif selected_door_color == 'blue':
            print('Before you is a sumptuous feast. You forget the treasure and tuck in. Game Over.')
        else:
            print('Invalid response. Game Over.')
