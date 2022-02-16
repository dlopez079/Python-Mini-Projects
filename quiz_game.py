# Welcome the player to the game.
print("Welcome to my computer quiz!")

# As the user if he or she would like to play.
playing = input("Do you want to play? ")

# Create a variable so we can keep track of the score.
score = 0

# Create a condition based on the answer that the user entered.
# If the user put anything else other than "yes" then the game will quit.
if playing.lower() != "yes":
    quit()

# Create a greeting for the user when they select yes.
print("Okay! Let's play :)")

# Ask a question #1 so the user can answer and save it to the variable.
# Increment score when user gets the correct answer.
answer = input("What nationality are you? ")
if answer.lower() == "puerto rican":
    print('Correct! You are Puerto Rican')
    score+= 1
else:
    print('Come One Bro.  Really!')

# Ask a question #2 so the user can answer and save it to the variable.
# Increment score when user gets the correct answer.
answer = input("What is Daddy's favorite baseball team? ")
if answer.lower() == "mets":
    print('Correct! His favorite team is the New York Mets!')
    score+= 1
else:
    print('Come One Bro.  Really! You need to move out!')

# Ask a question #3 so the user can answer and save it to the variable.
# Increment score when user gets the correct answer.
answer = input("Whos is the better parent? Mom or Dad? ")
if answer.lower() == "dad":
    print('You are correct again! Dad is always better')
    score+= 1
else:
    print('Kill Yourself!')

# Ask a question #4 so the user can answer and save it to the variable.
# Increment score when user gets the correct answer.
answer = input("What color is Daddy's car? ")
if answer.lower() == "blue":
    print('Correct! Daddys car is blue.  Fun Fact....He calls his car BLUE MAGIC')
    score+= 1
else:
    print('Come One Bro.  YOU SHOULD KNOW THIS!')

# Ask a question #4 so the user can answer and save it to the variable.
# Increment score when user gets the correct answer.
answer = input("What is your favorite? Soupy or Salad? ")
if answer.lower() == "soupy":
    print('Correct! Soupy')
    score+= 1
else:
    print('Come One Bro.  YOU SHOULD KNOW THIS!')

# Print out the final score.  Make sure you change the int to string.
print("Yout got " + str((score/5) *100) + "% Correct of this exam!")