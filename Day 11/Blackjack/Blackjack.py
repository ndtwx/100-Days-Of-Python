############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

import random
import os
from art import logo
print(logo)

#Deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
def deal_card(): 
    """return a random card from the list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#Calculate_score() function that takes a List of cards as input and returns the score. 
def calculate_score(cards): 
    """Take a list of cards and return the score calculated from the cards"""
    #Check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in the game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. 
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Compare() function that pass in the user_score and computer_score and compare both the scores to determine win or lose
def compare(user_score, computer_score):
    """Compare the score between the user and computer to determine the winner"""
    
    if user_score > 21 and computer_score > 21:
        return "BOTH WENT OVER! IT'S A DRAW!"

    if user_score == computer_score:
        return "IT'S A DRAW!"
    elif computer_score == 0:
        return "YOU LOSE, OPPONENT HAS BLACKJACK!"
    elif user_score == 0:
        return "YOU WIN WITH A BLACKJACK!"
    elif user_score > 21:
        return "YOU WENT OVER! YOU LOSE!"
    elif computer_score > 21:
        return "OPPONENT WENT OVER! YOU WIN!"
    elif user_score > computer_score:
        return "YOU WIN!"
    else:
        return "YOU LOSE!"

def play_game():
    """Main block of code"""
    print(logo)
    
    game_over = False
    user_cards = []
    computer_cards = []
    
    #Deal 2 cards each for the user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    #If the game is not over, it will continue until the user exit the game
    while not game_over:
        #Calculate the user and computer current score and see if there is any blackjack
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            #User will draw another card if no blackjack appear during the first two cards
            if input("Type 'y' to draw another card or 'n' to pass: ") == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                game_over = True
        
    #The computer will keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hands: {user_cards}, final_score: {user_score}")
    print(f" Computer's final hands: {computer_cards}, final_score: {computer_score}")
    print(compare(user_score, computer_score))

#Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack
while input("Do you want to play a game of Blackjack? Type 'y' to play or 'n' to exit: ") == "y":
    os.system('cls')
    play_game()


