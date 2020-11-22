import os
def clear(): os.system('clear')
from art import logo

print(logo)
print("Welcome to the silent auction.")
auction_pool = {}
auction_open = True

while auction_open:
  bidders_name = input("What is your name?\n")
  bid_value = int(input("What is your bid?\n$"))
  total_bidders = input("Are there anymore bidders? 'yes' or 'no'.\n")
  auction_pool[bidders_name] = bid_value
  if total_bidders == 'no':
    auction_open = False
    clear()
  else:
    clear()

#print(auction_pool)
highest_bidder = max(auction_pool.items(), key=lambda x : x[1])
print(f"{highest_bidder[0]} is the higest bidder with a bid of ${highest_bidder[1]}.")


