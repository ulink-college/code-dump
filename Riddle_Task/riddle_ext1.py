##########################################33
#   Riddle Task: Extending the program
#
#   Extension task 1: 
#   Have a selection of riddles stored that can be selected at random for the user
#

#imports:
import random

# Change the riddle and answer variables in to lists and populate with data
riddle = ["What has 4 eyes but cannot see? ", "What will break when you say its name? ", "The more you take, the more you leave behind. What are they? "]
answer = ["Mississippi","Silence","Footsteps"]

userAnswer = ""
attempt = 0
choice = random.randint(0,2)        #  use this variable to generate and store a number. This will be used for the list index
while userAnswer != answer[choice]:
    userAnswer = input(riddle[choice])
    attempt = attempt + 1
    if userAnswer!=answer[choice]:
        print("Sorry, that's not it.")
        print("You have had", attempt, "attempts.")

if attempt <= 3:
    print("Well done, you solved my riddle in 3 guesses")
else:
    print("Well done!")
