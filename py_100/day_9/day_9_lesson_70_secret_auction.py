# Day 9 Lesson 70: Secret Auction

import os

def clear_screen():
    os.system('clear')

bids = {}
# Every time I don't put state in a dictionary, it bites me.
state = {
    'keep_going': True
}

def keep_going():
    return state['keep_going'] 

def set_keep_going(val):
    state['keep_going'] = val 

def populate_bid():
    clear_screen()
    # prompt for name
    name = input('What is your name?\n\n')
    # prompt for bid
    bid = int(input('\n\nWhat is your bid?\n\n$'))
    bids[name]= bid
    # prompt for other bidders (are there any y/n)
    # We could handle invalid input here, but bigger fish to fry.
    set_keep_going(input('\n\nAre there any other bidders?\n\n') == 'y')

# welcome message
clear_screen()
print('Welcome to the Secret Auction')

# if yes: then clear screen and repeat
while keep_going() == True:
    populate_bid()

max_bid = 0
max_name = ''
for name, bid in bids.items():
    if bid > max_bid:
        max_bid = bid
        max_name = name

# if no: display the winner
clear_screen()
print(f'The winner of the Secret Auction is {max_name}, with a bid of ${max_bid}.\n\n')
