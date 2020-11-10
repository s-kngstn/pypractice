import random
print("Welcome to the Rock, Paper, Scissors game! Good luck, Have fun!")

player_choice = int(input("Please type 1 for rock, 2 for paper or 3 for scissors \n")) - 1
computer_choice = random.randint(0,2)


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



if computer_choice == player_choice:
  print("Tie. Please play again.")
elif computer_choice == 0 and player_choice == 1:
  print("Computer chooses: Rock")
  print(rock)
  print("You choose: Paper")
  print(paper)
  print("Paper beats Rock, Victory! YOU WIN!")
elif computer_choice == 1 and player_choice == 0:
  print("Computer chooses: Paper")
  print(paper)
  print("You choose: Rock")
  print(rock)
  print("Paper beats Rock, awww.. you lose :(")
elif computer_choice == 1 and player_choice == 2:
  print("Computer chooses: Paper")
  print(paper)
  print("You choose: Scissors")
  print(scissors)
  print("Scissors beats Paper, Victory! YOU WIN!")
elif computer_choice == 2 and player_choice == 1:
  print("Computer chooses: Scissors")
  print(scissors)
  print("You choose: Paper")
  print(paper)
  print("Scissors beats Paper, awww.. you lose :(")
elif computer_choice == 2 and player_choice == 0:
  print("Computer chooses: Scissors")
  print(scissors)
  print("You choose: Rock")
  print(rock)
  print("Rock beats Scissors, Victory! YOU WIN!")
elif computer_choice == 0 and player_choice == 2:
  print("Computer chooses: Rock")
  print(rock)
  print("You choose: Scissors")
  print(scissors)
  print("Rock beats Scissors, awww.. you lose :(")
else:
  print("Invalid entry, please choose again.")


