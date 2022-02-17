# Import a module called random.
# The random module comes with Python
import random

# Ask user for a number.
top_of_range = input("Type the highest possible number: ")

# Create an if statement that checks if it's a digit rather than a letter.
# Change the string input into an integer.  By default Python does not return an integer with user input. 
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    # Check to see if the user typed in a number larger than 0 since the range is between 0 and 11.
    if top_of_range <= 0: 
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type number next time.')
    quit()

# Generate a random number using a method called random.randint.
# I will pass a starting number and a stop number as parameters.
# random.randrange(start, stop)
# The stop number will never be used. 
# If you would like the range to start at 0, you can leave the start number out.
random_number = random.randint(0, top_of_range)

# Keep track of the amount of guess.
guesses = 0

# We want the user to continue to guess the number until he gets it right.  
# To do this, I will use a while loop. 
while True:
    # Everytime the while loop begins we will increment the guess count.
    guesses += 1

    # We will request users input
    user_guess = input("Make a guess: ")

    # If the user entered a digit, change it into an integer.
    if user_guess.isdigit():
        user_guess = int(user_guess)

    # If the user did not enter a digit, we will tell the user to type in a number.
    else:
        print("Please type a number next time.")
        continue
    
    # If the user guess equals the random number, the user wins and game is over.  We will use the break function to terminate game.
    if user_guess == random_number: 
        print("Congratulations! You got it!")
        break

    # If the user did not get it right, they will play again. 
    else:
        if user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")

# Print a statement that includes the amount of guesses.
print("You got it in", guesses, "guesses.")