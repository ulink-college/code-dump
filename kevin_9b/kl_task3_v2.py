time = 0
answer = ""
while answer != "Mississippi":
    print("What has 4 eyes but cannot see? ")
    print("Please entre the answer here:")
    answer = input()
    time+=1
    print("times:",time)
if answer == "Mississippi" and time <= 3:
    print("Well done, you solved my riddle within three guesses!")
elif answer == "Mississippi":
    print("Well down!You solve this riddle!")