# Score to grade converter:
enterScores = "Y"
while enterScores == "Y":
    print("Enter the final score: ")
    validInput = False
    while not validInput:
        score = input()
        if score.isnumeric():
            score = int(score)
            if score < 0 or score > 100:
                print("Must be between 0 & 100")  #Invalid range message
                print("Try again >> ")
            else:
                validInput = True
                if score > 95:
                    print("Grade = A*")
                elif score >= 85:
                    print("Grade = A")
                elif score >= 70:
                    print("Grade = B")
                elif score >= 60:
                    print("Grade = C")
                elif score >= 50:
                    print("Grade = D")
                elif score >= 40:
                    print("Grade = E")
                else:
                    print("Grade = U")
        elif score.upper() == "N":
            print("Byeeee!")
            enterScores = "N"
        else:
            print("You must enter an integer from 0 to 100")
