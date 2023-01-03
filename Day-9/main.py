from replit import clear
# HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

bids = {}
finish_auction = False
# dictionary bidding_record = {'Angela': 123, 'Alexandre': 234}
# Remember the loop through a dictionary check the Key
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        # First time bidder_amount will be 123 and then 234
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}, and the highest bid is {highest_bid}.")



while not finish_auction:
    name = input('What is your name? ')
    price = int(input('What is your bid? '))
    track_bids = 0
    bids[name] = price
    should_conitue = input("Are there any other bidders? 'yes' no' ").lower()
    if should_conitue == 'no':
        finish_auction = True
        find_highest_bidder(bids)
    elif should_conitue == 'yes':
        clear()
