import random

GUESSES = 5
RANDOM_NUMBER = random.randint(1, 100)

print("Welcome to the number guessing game.")

def get_guess():
    valid = False
    while not valid:
        guess = input("Guess what the random number is.  ")
        if int(guess) not in range(1, 100):
            print("Invalid input")
        else:
            valid = True
    return guess


guessed_number = get_guess()

while GUESSES >= 1:
    if RANDOM_NUMBER == guessed_number:
        print("You win!")
    elif GUESSES == 1:
        print("You lost! Better luck next time.")
        GUESSES -= 1
    else:
        GUESSES -= 1
        print("Try again. You have", GUESSES, "more guesses.")
        guessed_number = get_guess()