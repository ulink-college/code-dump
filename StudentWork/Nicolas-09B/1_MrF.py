riddle = "what has 4 eyes but cannot see?"
answer = "mississippi"
userAnswer = ""
attempt = 0
userAnswer = input(riddle)
while  userAnswer != answer:
    userAnswer = input(riddle)
    attempt += 1
    if userAnswer == answer:
        print("well done")
        if attempt <= 3:                  # take a look at this line...
                print("well done!!!!!")
            
    else:
        print("sorry,thats not the answer")
        print("You have had",attempt,"attempts")
