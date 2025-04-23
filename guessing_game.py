'''FUNCTION GuessingGame
    // Initialize the game
    SET secret_number to a random integer between 1 and 10
    SET guesses_left to 5
    SET user_guess to 0
    
    // Display welcome message
    DISPLAY "Welcome to the Guessing Game!"
    DISPLAY "I'm thinking of a number between 1 and 10."
    DISPLAY "You have " + guesses_left + " guesses to find it."
    
    // Main game loop
    WHILE guesses_left > 0 AND user_guess != secret_number DO
        TRY
            // Get and validate user input
            INPUT user_guess as integer with prompt showing guesses left
            
            IF user_guess < 1 OR user_guess > 10 THEN
                DISPLAY "Please guess a number between 1 and 10."
                CONTINUE to next iteration
            END IF
            
            // Check if guess is correct
            IF user_guess equals secret_number THEN
                DISPLAY "Congratulations! You've guessed the number!"
            ELSE IF user_guess < secret_number THEN
                DISPLAY "Too low!"
            ELSE
                DISPLAY "Too high!"
            END IF
            
            // Update guesses remaining
            DECREMENT guesses_left by 1
            
            // Inform user of remaining guesses
            IF guesses_left > 0 THEN
                DISPLAY "You have " + guesses_left + " guesses left."
            ELSE
                DISPLAY "Sorry, you've run out of guesses. The number was " + secret_number + "."
            END IF
            
        CATCH ValueError
            DISPLAY "Invalid input. Please enter a number between 1 and 10."
        END TRY
    END WHILE
END FUNCTION

CALL GuessingGame'''

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
