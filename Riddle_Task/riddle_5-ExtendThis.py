################################
# EXTEND THIS CODE!!
#
# Modify this code so that:
#       -- there are multiple questions
#       -- the questions have matching answers
#       -- the user gets a random question each time the code is run
#       -- make it so that the user gets asked if they want to play again, 
#           and then another question is picked
# 
riddle = "What has 4 eyes but cannot see? "
answer = "Mississippi"
userAnswer = ""
attempt = 0

while userAnswer != answer:
    userAnswer = input(riddle)
    attempt = attempt + 1
    if userAnswer == answer:
        print("Well done!")
        # Extend the program so that if the answer is correct and the attempts is 3 or fewer it displays on message
    else:
        print("Sorry, that's not it.")
        print("You have had", attempt, "attempts.")


## EXTENSION: BONUS house points if you can re-write this code in a different way. 
#  There are alternative ways of writing this program, some probably more effective than this!
