##########################################33
#   Riddle Task: Extending the program
#
#   Extension task 2: 
#   When the user guesses correctly ask if they would like to play again
#

#imports:
import random

# Change the riddle and answer variables in to lists and populate with data
riddle = ["What has 4 eyes but cannot see? ", "What will break when you say its name? ", "The more you take, the more you leave behind. What are they? "]
answer = ["Mississippi","Silence","Footsteps"]

attempt = 0
again = "Y"

while again == "Y":
    userAnswer = ""
    choice = random.randint(0,2)        #  use this variable to generate and store a number. This will be used for the list index
    print(choice)
    while userAnswer != answer[choice]:
        userAnswer = input(riddle[choice])
        attempt = attempt + 1
        if userAnswer == answer[choice]:
            print("Well done!")
        else:
            print("Sorry, that's not it.")
            print("You have had", attempt, "attempts.")
    again = input("Play again? Y or N: ").upper()

