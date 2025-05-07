from os import system
from art import logo
print(logo)
bids = {}
bidding_finished = False

# Function to find the highest bidder
def find_highest_bidder(bidding_record):
    # {"Angela: 123, "James": 321}
    highest_bid=0
    winner = ""
    # This for loop will be looping through each key from the dictionary
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


# The following code will run until the bidding is finished
while not bidding_finished:
    # Ask for name input
    name = input ("What is your name?: ")
    
    # Ask for bid price
    price = int(input ("What is your bid?: $"))

    # Add Name and Bid into a dictionary
    bids[name] = price

    # Ask if there are other users who want to bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue=="yes":
        system('clear')

