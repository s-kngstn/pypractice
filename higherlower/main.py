from game_data import data
from art import logo, vs
import random
import os

#Clear screen
def clear(): 
  os.system('clear')

# Create a random int module and assign it to a variable with a range of total items in data pool
def rand_num(): 
  '''Create a random number between 0 & 49'''
  return random.randint(0,49)

#Start Game
def start():

  # Make two lists for each data set to go into
  compare = []
  against = []

  # Add data to each list at random
  compare.append(data[rand_num()])
  against.append(data[rand_num()])

  # Create a function to replace old data with new
  def replace():
      '''Remove data from list and replace it with new data'''
      against.remove(against[0])
      against.append(data[rand_num()])
      #print(against)

  # Start game loop
  gameon = True
  score = 0
  while gameon:
    # if both items match, we replace one at random  
    while compare == against:
      # print("bug fix: against and compare matched, re-shuffling....")
      replace()

    # Create variables for the account name, follower count, description and country
    compare_name = compare[0]["name"]
    compare_count = compare[0]["follower_count"]
    compare_country = compare[0]["country"]
    compare_description = compare[0]["description"]
    against_name = against[0]["name"]
    against_count = against[0]["follower_count"]  
    against_country = against[0]["country"]
    against_description = against[0]["description"]

    # Game Display
    print(logo)
    print(f"Compare A: {compare_name}, a {compare_description}, from {compare_country}")
    print(vs)
    #print(f"Cheatsheet Follower Count: {compare_count}")
    print(f"Against B: {against_name}, a {against_description}, from {against_country}")
    #print(f"Cheatsheet Follower Count: {against_count}")

    # User inputs choice
    most_followers = input("Who has more followers? 'A' or 'B': ").lower()

    # Check which follower count is higher
    if most_followers == 'a':
      if compare_count > against_count:
        clear()
        score += 1
        print(f"You're right! Score: {score}")
        replace()
      else:
        print(f"Wrong. Game Over. Total Score: {score}")
        gameon = False
    elif most_followers == 'b':
      if compare_count < against_count:
        clear()
        score += 1
        print(f"You're right! Score: {score}")
        compare.remove(compare[0])
        compare.append(against[0])
        replace()
      else:
        clear()
        print(f"Wrong. Game Over. Total Score: {score}")
        gameon = False
    else:
      clear()
      print(f"{most_followers} is an Invalid input")
      gameon = False

start()

