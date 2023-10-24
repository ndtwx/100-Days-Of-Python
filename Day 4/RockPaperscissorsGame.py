import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
a = "Rock"
b = "Paper"
c = "Scissors"
game_string = [a, b, c]
game_images = [rock, paper, scissors]
user_choice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

while user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number!")
  user_choice = int(input("Please type a valid number. Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
      
else:
    print(f"you chose: {game_string[user_choice]}")
    print(game_images[user_choice])

    computer_choice = int(random.randint(0,2))
    print(f"Computer chose: {game_string[computer_choice]}")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")


