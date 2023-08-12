from logo import logo

print(logo)
is_audition_on = True
bids = {}

while is_audition_on:
    get_user_name = input("What is your name? ")
    get_user_bid = int(input('What is your bid? '))
    bids[get_user_name] = get_user_bid

    get_still_bid = input("Are there any other bid? Type (Yes) (No)").lower()

    if get_still_bid == "no":
        is_audition_on = False

highest_bid = 0
winner = ""
for name, bid in bids.items():
    if bid > highest_bid:
        highest_bid = bid
        winner = name

print(f"The winner with the highest bid is {winner} with a bid of {highest_bid}.")
