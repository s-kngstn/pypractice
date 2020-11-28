import random

answer = random.randint(1, 100)                                                                                  
print("Welcome to the Number Guessing Game!")                                    
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
                                                                                 
if difficulty == 'easy':                                                         
  guess_count = 10
else:       
  guess_count = 5     

#print(f"Testing purposes: Answer is {answer}")
print(f"You have {guess_count} attempts remaining to guess the number.")                             
guess = int(input("Make a guess: "))

guesses_left = True
while guess_count > 1 and guesses_left:
  if guess == answer:
    guesses_left = False
    print(f"You guessed {answer}, Thats the correct number! YOU WON!")
  elif guess > answer:            
    guess_count -= 1
    print(f"You guessed too high. Try again. {guess_count} guesses left.")
    guess = int(input("Make a guess: ")) 
  elif guess < answer:                                                         
    guess_count -= 1                                                          
    print(f"You guessed too low. Try again. {guess_count} guesses left.")   
    guess = int(input("Make a guess: "))                                                                    

if guess_count == 1:
  print(f"You're out of guesses. I was thinking of {answer}. You lose.")
