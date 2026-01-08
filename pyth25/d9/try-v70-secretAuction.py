import os
import art

print(art.logo)

# function to clear screen (works on Windows, Mac, Linux)
def clear_screen():
          print("\n" * 10000)

bids = {}

while True:
    print("Welcome to the bidding program ......")
    name = input("Enter your name: ")
    price = int(input("Enter your bid price: $"))

    # store in dictionary
    bids[name] = price

    more = input("Are there more bidders? Type 'yes' or 'no': ").lower()

    if more == "yes":
        clear_screen()  # hide previous bidder's input
    elif more == "no":
        break
    else:
        print("Invalid input, ending program...")
        break

# print final results
print("\n=== Auction Results ===")
for person, amount in bids.items():
    print(f"{person}: ${amount}")

# determine highest bidder
winner = max(bids, key=bids.get)
print(f"\nWinner is {winner} with a bid of ${bids[winner]}!")