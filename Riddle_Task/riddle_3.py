riddle = "What has 4 eyes but cannot see? "
answer = "Mississippi"
userAnswer = ""
attempt = 0
userAnswer = input(riddle)
attempt += 1
if userAnswer == answer:
    print("Well done!")
else:
    print("You have had", attempt, "attempts.")
