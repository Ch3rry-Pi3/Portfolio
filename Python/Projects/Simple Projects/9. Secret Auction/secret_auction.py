"""
Secret Auction Program

This program allows multiple users to place secret bids for an auction. The winner is 
determined by finding the highest bid. The program continues accepting bids until 
all bidders have participated.
"""

from art import logo

# Display the logo
print(logo)


def find_highest_bidder(bidding_record):
    """
    Determines the highest bidder and their bid amount.

    Parameters:
        bidding_record (dict): A dictionary containing bidder names as keys and their bids as values.

    Returns:
        None: Prints the winner and the highest bid to the console.
    """
    highest_bid = 0
    winner = ""
    
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


# Initialise an empty dictionary to store bids
bids = {}
continue_bidding = True

# Main bidding loop
while continue_bidding:
    # Get the bidder's name and bid amount
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price

    # Ask if there are other bidders
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        # Clear the screen (simulate by printing blank lines)
        print("\n" * 20)
