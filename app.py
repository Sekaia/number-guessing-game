import random


guesses = 5
random_number = random.randint(1, 100)
print("Welcome to the number guessing game.")
guessed_number = input("Guess what the random number is.  ")

while guesses >= 1:
    if random_number == guessed_number:
        print("You win!")
    elif guesses == 1:
        print("You lost! Better luck next time.")
        guesses -= 1
    else:
        guesses -= 1
        print("Try again. You have", guesses, "more guesses.")
        guessed_number = input("Guess what the random number is.  ")