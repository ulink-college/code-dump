# Rock, paper, scissors
#
# Create a console/terminal version of rock, paper, scissors
# It is you versus the computer...who will win?

# ***Requirements***
# Allow the user to enter their choice
# Compare to the computers selection
#    Rock beats scissors
#    Scissors beats paper
#    Paper beats rock
#
# Tell the user the result
#
# Extensions....
#   Keep track of score
#   Save a leader board
#   option to play best out of three or continuous

import random as r

z = "*"
print(z*35 + """
  Welcome to Rock, Paper Scissors!
""" + z*35)

choices = ["Rock","Paper","Scissors"]       #Array for the choices
compChoice = choices[r.randint(0,2)]        #Get cpmputer generated selection
playerChoice = input("Enter your choice - [R]ock, [P]aper or [S]cissors: ")

#check player v computer and output response
print(compChoice)
if playerChoice == "R":
    if compChoice == "Rock":
        print("Draw")
    elif compChoice == "Paper":
        print("You lose!")
    elif compChoice == "Scissors": 
        print("You win!")
    
    
    #choice[random.randint(0,2)]
