from art import logo
bids = {}
print(logo)
print("Welcome to the auction program.")
name = input("What is your name: ")
bid = input("What's your bid: $")
bids[name] = bid
other_bidder = input("Are there other bidders? Type 'yes' or 'no'.")
while other_bidder == 'yes':
    print('\n' * 100)
    name = input("What is your name: ")
    bid = input("What's your bid: $")
    bids[name] = bid
    other_bidder = input("Are there other bidders? Type 'yes' or 'no'.")
print(f"The winner is {max(bids, key=bids.get)} with a bid of ${bids[max(bids, key=bids.get)]}")