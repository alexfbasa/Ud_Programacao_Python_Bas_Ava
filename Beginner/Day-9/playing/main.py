from replit import clear
from art import logo

print(logo)

auction = {}
is_auction_on = True


def get_bides():
    get_name = input('Please, type your name: ')
    get_user_bid = float(input("Type your bid:$"))
    auction[get_name] = get_user_bid


def find_highest_bid(bid_record):
    highest_bid = 0
    winner = ""
    for bid in bid_record:
        bid_amount = bid_record[bid]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bid
    print(f"The winner is {winner}, and the highest bid is {highest_bid}.")


while is_auction_on:
    print("Let's get started the Auction:")
    get_bides()
    another_bid = input("Is there another bid? (Yes) (No) ").lower()
    if another_bid == "yes":
        clear()
        pass
    else:
        find_highest_bid(auction)
        is_auction_on = False
