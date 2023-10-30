#import os module so that we can use the clear function to clear screen after restart
import os
from art import logo

print(logo)

bids = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    # loop through each key instead of the key value
    for bidder in bidding_record: 
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
           highest_bid = bid_amount
           winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

#While loop that continues to execute the program if the user types 'yes'.
should_end = False
while not should_end:
  name = input("What is your name?: ")
  # convert to integer so we can use it for comparsion
  price = int(input("What is your bid?: $")) 
  #Create a dictinoary where the name is the key 
  #price is the value 
  bids[name] = price

  #Ask the user if they want to restart the program,
  #if they type 'yes' then the program will restart until they type no.
  restart = input("Are there any other bidders? Type 'yes' or 'no.\n")
  if restart == "no":
    should_end = True
    find_highest_bidder(bidding_record = bids)
  elif restart == "yes":
    os.system('cls')

    
  

  
  


