import random

#TODO: Fix guessed number check

GUESSES = 5
RANDOM_NUMBER = random.randint(1, 100)

print("Welcome to the number guessing game.")

valid = False
while not valid:
    guessed_number = input("Guess what the random number is.  ")
    #why wont this work?
    if guessed_number in range(1, 100):
        print("oh")
    else:
        #always getting this message
        print("Invalid input")


while GUESSES >= 1:
    if RANDOM_NUMBER == guessed_number:
        print("You win!")
    elif GUESSES == 1:
        print("You lost! Better luck next time.")
        GUESSES -= 1
    else:
        GUESSES -= 1
        print("Try again. You have", GUESSES, "more guesses.")
        guessed_number = input("Guess what the random number is.  ")