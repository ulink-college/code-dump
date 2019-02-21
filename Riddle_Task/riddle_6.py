riddle = "What has 4 eyes but cannot see? "
answer = "Mississippi"
userAnswer = ""
attempt = 0

while userAnswer != answer:
    userAnswer = input(riddle)
    attempt = attempt + 1
    if userAnswer == answer:
        #add new selection for if attempt <= 3
        if attempt <= 3:
            print("Well done, you solved my riddle in 3 guesses")
            break               #   when this line runs python wil exit the 'while' loop
        else:
            print("Well done!")
            break               # need to remember it here too
    else:
        print("Sorry, that's not it.")
        print("You have had", attempt, "attempts.")
