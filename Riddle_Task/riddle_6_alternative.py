riddle = "What has 4 eyes but cannot see? "
answer = "Mississippi"
userAnswer = ""
attempt = 0

#This will run so long as the user does not answer correctly
while userAnswer != answer:
    userAnswer = input(riddle)
    attempt = attempt + 1
    if userAnswer != answer:
        print("Sorry, that's not right.")
        print("You have had", attempt, "attempts.")

#Move the slection outside of the loop
# Once the user get the answer, python exits the loop this code gets run.
# This is an alternative sequence for the code

if attempt <= 3:
    print("Well done, you solved my riddle in 3 guesses")
else:
    print("Well done!")
