# The user is going to select from Rock, Paper and Sciccors
# The computer is going to keep track of the amount of times either the computer or the user wins.

import random

# We need two variables; one for the user wins and one for the cpu wins
user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

# I'm going to start a while loop to capsulate the game.
while True:

    # Capture users input and save it to a variable.  
    # We will make sure that the input is in all lower case.
    user_input = input("Type Rock/Paper/Scissors or Q to Quit: ").lower()

    # If the user selects "q" then the game will break out of the while loop which will end the game..
    if user_input == "q":
        break

    # If the user selects anything other than rock, paper, scissor, then use continue to start the while loop again.
    if user_input not in options:
        continue

    # Generate a random number between three selections
    # Use the Random method with a start point of 0 and a stop point of 2.  
    # This means, there can be either rock: 1, paper: 2, or, scissors 3.
    # The random number will become the index of the list of options.
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    # User Winning Condition 1
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
       
    # User Winning Condition 2
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    # User Winning Condition 3
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    
    # You check for the three winning conditions for the user. 
    # Anything after that the computer wins so there is no need to check any other condition.
    else: 
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")