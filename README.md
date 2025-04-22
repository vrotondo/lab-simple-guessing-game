# lab-simple-guessing-game
Foundations I - Lab: Simple Guessing Game

Lab: Simple Guessing Game 
Welcome to the Simple Guessing Game lab! In this exercise, you'll apply your knowledge of while loops in Python to create an interactive guessing game. This lab will reinforce your understanding of loop conditions, user input handling, and basic game logic.

As a software engineer, you've been tasked with developing a simple guessing game for a mobile app. Users will guess a secret number within a limited number of attempts. This lab will guide you through implementing this game using while loops in Python. In this lab, you will implement a while loop to control game flow, generate random numbers, handle user input, and apply conditional statements within a loop structure.

Problem Statement
For this lab, you will create a Python program that generates a random secret number between 1 and 10 (inclusive) and allows the user to guess it within five attempts. Provide feedback to the user based on whether the guess is too high, too low, or correct. The game should continue prompting for guesses until the user wins or exhausts their attempts.

Game Requirements:

Generate a random secret number between 1 and 10.
Allow only five attempts.
Provide feedback to the user if their guess is too high, too low, or correct.
Tools and Resources
Use a Python IDE (VS Code) locally to complete this lab.
Instructions
Step 1: Define
Break down the problem into smaller, manageable tasks:

Identify the main components of the game:
Random number generation
User input handling
Guess comparison
Attempt tracking
Feedback provision
List the variables you'll need:
Secret number
User's guess
Number of attempts remaining
Outline the main game loop structure
Think about how these components will interact and what information needs to be tracked throughout the game.

Step 2: Design 
Plan your approach:

Sketch out the flow of your game using pseudocode or a flowchart.
Decide on the structure of your while loop:
What condition will keep the loop running?
What actions will be performed in each iteration?
Plan how you'll handle different scenarios:
Correct guess
Incorrect guess (too high/too low)
Running out of attempts
Your design should clearly show how the game progresses from start to finish, including all possible outcomes.

Step 3: Develop
Create a script that integrates all the steps for create a while loops lab. 

1. Import the Necessary Module
To develop a game link this you should import the random module . At the beginning of your script, you'll need to import the random module from Python's standard library. This module provides functions for generating random numbers, which is essential for creating the secret number in the guessing game.

Use the following command to import the necessary module: 

import random
2. Generate the Secret Number
Use the following command to generate the secret number:

secret_number = random.randint(1, 10)
This line stores the generated random number in the variable secret_number. This is the number the user will try to guess.

You will use the random.randint(a, b) function to generate a random integer between the two specified values and inclusive of the values.

In this lab, you will use a number between 1 and 10 (inclusive). 

3. Define Variables
Create the following variables to keep track of the game state:

guesses_left This variable holds the number of guesses remaining for the user. It's initialized to 5, allowing for five attempts.
user_guess This variable will store the user's guess during each round of the game. It's initially set to 0.
4. Implement the While Loop
The core of the game logic is implemented using a while loop. This loop will continue to run as long as the user has guesses remaining (guesses_left > 0).
Make sure your indentation is correct as it's crucial in Python. 
5. Integrate Input and Outputs
Inside the while loop, prompt the user to guess a number.
To do this, use the following function: input().
Note that the input() function returns a string by default. To compare it with the secret number (which is an integer), convert it to an integer.
To convert input() to an integer, use int().
6. Display Results
Use an if statement to check if (user_guess) matches the secret number (secret_number).

If the guess is correct (user_guess == secret_number):
Print a congratulatory message of: “Congratulations! You guessed the number!”
Use the break statement to exit the loop when the game is won.

If the guess is higher than the secret number (user_guess > secret_number):
Print a message: "Too high! Try again."
Otherwise, use an else statement:

Print a message of: "Too low! Try again."
Step 4: Test and Refine
Run your program multiple times to test different scenarios:
Guessing the number correctly
Running out of guesses
Guessing numbers too high and too low
Verify that:
The secret number is always between 1 and 10
The user only gets 5 attempts
Appropriate feedback is given for each guess
The game ends correctly (win or lose)
Refine your code if you find any issues or areas for improvement.
Step 5: Document and Maintain
Version Control: Use version control to track changes; allowing for easy updates, collaborative editing, and the ability to revert to previous versions if necessary.

Regular Updates and Reviews: Schedule regular reviews and updates for code ensure content remains relevant, accurate, and aligned with the latest Python developments and industry practices, 

Documentation and Examples Repository: Maintain a centralized repository containing all lab documents, example code, and solutions. 

Submission
When you have completed all the steps and saved your final draft as guessing_game.py, launch CodeGrade to upload your submission by clicking theSimple Guessing Game- While Loops Lab button below.
Upload your Python file to the click here or add files to upload field. 
For additional information on submitting assignments in CodeGrade: Getting Started in CanvasLinks to an external site..
Grading Criteria
Use the rubric below as a guide for how this lab is graded.
You submission will be automatically scored in CodeGrade.
You can review your submission in CodeGrade and see your final score in your Canvas grades.
