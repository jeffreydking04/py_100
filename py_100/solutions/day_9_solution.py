# Day 9: Project: Secret Auction

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
    name = input('What is your name?\n\n')
    bid = int(input('\n\nWhat is your bid?\n\n$'))
    bids[name]= bid
    # We could handle invalid input here, but bigger fish to fry.
    set_keep_going(input('\n\nAre there any other bidders?\n\n') == 'y')

clear_screen()
print('Welcome to the Secret Auction')

while keep_going() == True:
    populate_bid()

# max_bid = 0
# max_name = ''
# for name, bid in bids.items():
#     if bid > max_bid:
#         max_bid = bid
#         max_name = name

# clear_screen()
# print(f'The winner of the Secret Auction is {max_name}, with a bid of ${max_bid}.\n\n')

# So this is neat baked in functionality, I don't think js has this.
# Although that is sure non-intuitive syntax on the key.
winner = max(bids, key=bids.get)
clear_screen()
print(f'The winner of the Secret Auction is {winner}, with a bid of ${bids[winner]}.\n\n')
