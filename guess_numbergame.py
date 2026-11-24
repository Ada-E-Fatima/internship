# #------------------------Guessing the number game------------------------#
# import random

# secret_number = random.randint(1, 20)              # It gives a random number between 1-20
# # Number of guesses are not more than 5
# print("-----------------Take a guess between 1- 20--------------- ")
# for guesses_taken in range(1, 6):
#     guess = int(input("Enter your guess:"))
#     if guess == secret_number:               # if guess is correct
#         print(f"Congratulations! you guessed correct.....")
#         print(f"The number you guesses is {secret_number}, and you guessed it in {guesses_taken} attempts")
#         break
#     elif guess < secret_number:                 # if guess is less than the secret number
#         print("Too low!")
#     else:                                        # else guess is greater than the secret number
#         print("Too high!")


# #-----------------------IF THE USER HAS USED ALL THE ATTEPMTS-----------------------#
# if guesses_taken == 5 and guess != secret_number:
#      print(f"You have used all your attempts, The number was {secret_number}. Better luck next time!")



  

    
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
    if guess == secret_number:
        won = True
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

if won:
    print(f"Congratulations! You guessed {secret_number} in {guesses_taken} attempt(s).")
else:
    print(f"Out of attempts. The number was {secret_number}. Better luck next time!")