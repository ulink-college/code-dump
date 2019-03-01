time = 0
answer = ""
while answer != "Mississippi":
    print("What has 4 eyes but cannot see? ")
    print("Please entre the answer here:")
    answer = input()
    if answer!="Mississippi":
        time+=1
        print("Number of %s times: %d times"%('error',time))
    elif answer == "Mississippi" and time+1 <= 3:
        print("Well done, you solved my riddle within three guesses!Number of total times: %d times"%(time + 1))
        print("Do you want to cotinue? Reply Yes or No")
        break
    elif answer == "Mississippi":
        print("Well down!You solve this riddle!Number of total times: %d times"%(time + 1))
        print("Do you want to cotinue? Reply Yes or No")
        break
time2 = 0
answer1 = input()
while answer1 == "Yes":
    print("What will break when you say its name?  ")
    print("Please entre the answer here:")
    answer2 = input()
    if answer2!="Silence":
        time2+=1
        print("Number of %s times: %d times"%('error',time2))
    elif answer2 == "Silence" and time2+1 <= 3:
        print("Well done, you solved my riddle within three guesses!Number of total times: %d times"%(time2 + 1))
        print("Do you want to cotinue? Reply Yes or No")
        break
    elif answer2 == "Silence":
        print("Well down!You solve this riddle!Number of total times: %d times"%(time2 + 1))
        print("Do you want to cotinue? Reply Yes or No")
        break
time3 = 0
answer3 = input()
while answer3 == "Yes":
    print("The more you take, the more you leave behind. What are they?  ")
    print("Please entre the answer here:")
    answer4 = input()
    if answer4!="Footsteps":
        time3+=1
        print("Number of %s times: %d times"%('error',time3))
    elif answer4 == "Footsteps" and time3+1 <= 3:
        print("Well done, you solved my riddle within three guesses!Number of total times: %d times"%(time3 + 1))
        break
    elif answer4 == "Footsteps":
        print("Well down!You solve this riddle!Number of total times: %d times"%(time3 + 1))
        break        
