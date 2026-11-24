# #------------------------Guessing the number game------------------------#   
import random

MAX_GUESSES = 5                      # change the limit in one place
secret_number = random.randint(1, 20)
guesses_taken = 0
won = False

print("----- Guess the number between 1 and 20 -----")

while guesses_taken < MAX_GUESSES and not won:
    text = input("Enter your guess: ")
    if not text.isdigit():           # protects against letters/empty input
        print("Please enter a whole number.")
        continue                     # does not count as an attempt
    guess = int(text)
    if guess < 1 or guess > 20:
        print("Number must be between 1 and 20.")
        continue
    guesses_taken += 1
    if guess == secret_number:                # If guess is correct
        won = True
    elif guess < secret_number:                # If guess is less than the secret number
        print("Too low!")
    else:                                       # At last if guess is greater than secret number
        print("Too high!")

if won:
    print(f"Congratulations! You guessed {secret_number} in {guesses_taken} attempt(s).")
  #-----------------------IF THE USER HAS USED ALL THE ATTEPMTS-----------------------#
else:
    print(f"Out of attempts. The number was {secret_number}. Better luck next time!")
