from art import logo
import random
import os
def clear(): os.system('clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start_game = input("Do you want to play a game of Black Jack? Type 'y' or 'n': ")
# Draw a random card from the card list
def drawcard():
  return random.choice(cards)
# Calculate the total integers from a list
def card_total(list):
  total = 0
  for num in list:
    total += num
  return total
  
def start():
  print(logo)
  # User and Computer Empty Lists
  user_cards = []
  dealer_cards = []

  # Add two cards to user list
  user_cards.append(drawcard())
  user_cards.append(drawcard())
  user_total = card_total(user_cards)
  print(f"Users cards: {user_cards}")
  #print(f"User Card Total: {user_total}")
  # Add two cards to dealer list
  dealer_cards.append(drawcard())
  dealer_cards.append(drawcard())
  dealer_total = card_total(dealer_cards)
  print(f"Dealers first card: {dealer_cards[0]}")
  #print(f"Dealer Card Total: {dealer_total}")

  # Does the user or computer have a Blackjack?
  if user_total == 21 and dealer_total != 21:
    print("Blackjack! You win!")
  elif user_total == 21 and dealer_total == 21:
    print("You lose. Dealer has Blackjack")
  elif user_total != 21 and dealer_total == 21:
    print("You lose. Dealer has Blackjack.")

  # Is the user's score over 21?
  play = True
  while user_total > 21 and play:
    if 11 in user_cards:
      for n, i in enumerate(user_cards):
        if i == 11:
          user_cards[n] = 1
          user_total = card_total(user_cards)
          if user_total > 21:
            #print("You went over 21! You lose.")
            user_total = card_total(user_cards)
          else:
            hit_or_hold = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit_or_hold == 'y':
              user_cards.append(drawcard())
              user_total = card_total(user_cards)
              #print(f"Over 21 total after second card pick {user_total}")
              print(f"Users cards: {user_cards}")
            else:
              user_total = card_total(user_cards)
              play = False
      print(f"TESTING PURPOSES: {user_cards, user_total}")
    else:
      user_total = card_total(user_cards)
      play = False 
  
  # Is user's score under 21?
  while user_total < 21 and play:
    hit_or_hold = input("Type 'y' to get another card, type 'n' to pass: ")
    if hit_or_hold == 'y':
      user_cards.append(drawcard())
      user_total = card_total(user_cards)
      #print(f"Under 21 total after second card pick {user_total}")
      print(f"Users cards: {user_cards}")
      if user_total > 21:
        #print("You went over 21, you lose.")
        user_total = card_total(user_cards)
    else:
      user_total = card_total(user_cards)
      play = False

  print(f"User final cards: {user_cards} | User total: {user_total}")

  # Dealer Plays
  while dealer_total != 0 and dealer_total < 16:
    dealer_cards.append(drawcard())
    dealer_total = card_total(dealer_cards)

  print(f"Dealer final cards: {dealer_cards} | Dealer total: {dealer_total}")

  if user_total > 21:
    print("Bust! You went over 21, you lose.")
  elif user_total == dealer_total:
    print("It's a tie.")
  elif user_total <= 21 and dealer_total > 21:
    print("You win! Dealer went bust!")
  elif dealer_total > user_total and dealer_total <= 21:
    print("Dealer wins!")
  elif user_total > dealer_total:
    print("You win!")
  
  play_again = input("Would you like to play again? Type 'y' for yes, or 'n' to quit: ")
  if play_again == 'y':
    clear()
    start()
  else:
    clear()

if start_game == 'y':
  start()
