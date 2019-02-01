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
    elif answer == "Mississippi":
        print("Well down!You solve this riddle!Number of total times: %d times"%(time + 1))