# Slash Mark Python Internship (Beginner: Task 2)

import random # Import the random module to generate random numbers
import time # Import the time module for pausing execution

def intro():
    # Display welcome message and instructions
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    time.sleep(0.5) # Pause for 0.5 seconds
    print("Try to guess the number!")

def pick_number():
    # Generate a random number between 1 and 100
    return random.randint(1, 100)

def get_guess():
    # Function to get user's guess and validate it
    while True:
        guess = input("Enter your guess: ") # Prompt the user for a guess
        if guess.isdigit(): # Check if the input is a positive integer
            return int(guess)  # Return the guess as an integer
        else:
            print("Invalid input. Please enter a valid number.") # Display error message

def play_game():
    # Main game logic
    number = pick_number() # Pick a random number
    guesses_taken = 0 # Initialize the number of guesses taken by the player

    while True:
        guess = get_guess() # Get the user's guess
        guesses_taken += 1 # Increment the number of guesses taken

        if guess < number:
            print("Too low! Try again.") # Display a message if the guess is too low
        elif guess > number:
            print("Too high! Try again.") # Display a message if the guess is too high
        else:
            print(f"Congratulations! You guessed the number in {guesses_taken} guesses.")
            break # Break out of the loop if the guess is correct

def main():
    while True:
        intro() # Display the introduction and instructions
        play_game() # Play the game
        
        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (yes/no): ")
        
        # Validate the player's input
        while play_again.lower() not in ["yes", "no"]:
            print("Invalid choice. Please select 'yes' or 'no'.") # Display error message
            play_again = input("Do you want to play again? (yes/no): ") # Prompt again
            
        # If the player chooses not to play again, end the game
        if play_again.lower() == "no":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main() # Run the main function when the script is executed
