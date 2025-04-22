import random

# Generate secret number
secret_number = random.randint(1, 10)

# Define variables
guesses_left = 5
user_guess = 0

# Implement the while loop
print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
print(f"You have {guesses_left} guesses to find it.")

while guesses_left > 0 and user_guess != secret_number:
    # Get user input
    try:
        user_guess = int(input(f"Enter your guess (1-10), {guesses_left} guesses left: "))

        # Check if guess is in valid range
        if user_guess < 1 or user_guess > 10:
            print("Please guess a number between 1 and 10.")
            continue

        # Check if guess is cor
        if user_guess == secret_number:
            print("Congratulations! You've guessed the number!")
        elif user_guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
        
        # Decrease the remaining guesses
        guesses_left -= 1

        # Inform user of remaining guesses
        if guesses_left > 0:
            print(f"You have {guesses_left} guesses left.")
        else:
            print(f"Sorry, you've run out of guesses. The number was {secret_number}.")
        
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 10.")