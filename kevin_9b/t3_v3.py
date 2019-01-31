time = 0
answer = ""
while answer != "Mississippi":
    print("What has 4 eyes but cannot see? ")
    print("Please enter the answer here:")
    answer = input()
    time+=1
    
    if answer == "Mississippi" and time <= 3:
        print("Well done, you solved my riddle within three guesses! Number of times: %d times"%(time))
    elif answer == "Mississippi":
        print("Well done! You solved this riddle! Number of times: %d times"%(time))
    else:
        print("Number of %s times: %d times"%('error',time))