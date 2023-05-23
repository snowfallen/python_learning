from art import logo


def clear():
    print("\n" * 50)
    
bids: dict = {}
bidding_finished: bool = False


def find_highest_bidder (bidding_record):  
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
     
while not bidding_finished:
    print(logo) 
    name = str(input("What is your name ? "))
    price = int(input("What is your bid ? "))
    bids[name] = price
    should_continue = input("Are there any other bidders ? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
    