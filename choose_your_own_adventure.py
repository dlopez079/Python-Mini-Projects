name = input('Type Your Name: ')
print("Welcome,", name, "to this adventure!")

answer = input('Your are on a dirt road, it has come to and end and you can go left or right.  Which way would youl like to go? ').lower

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across?  Type walk to walk around and swim to swim accross: ")

    if answer == "swim": 
        print("You swam across and was eaton by an alligator. ")
    elif answer == "walk": 
        print("You walk for many miles, ran out of water and lost the game.")
    else: 
        print("Not a valid option. You lose.")  
        
elif answer == "right":
    print("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)?")

    if answer == "back": 
        print("You go back and lose.")
    elif answer == "cross": 
        answer = input("You cross the bridge and meet a stranger. Do you want to talk to them (Yes,No)?")

        if answer == "yes": 
            print("You talk to the stranger and they give you gold.  You Win!")
        elif answer == "no": 
            print("You ignore the stranger and they get offended.  You lose!")
        else: 
            print("Not a valid option.  You lose.") 

    else: 
        print("") 
else: 
    print("Not a valid option. You lose.")

print("Thank you for trying", name)