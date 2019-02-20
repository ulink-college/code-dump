time = 0 
answer = "" 
while answer != "Mississippi": 
    print("What has 4 eyes but cannot see? ") 
    print("Please entre the answer here:") 
    answer = input() 
    time+=1 
    if answer == "Mississippi":
        if time <= 3:
            print("Well done, you solved my riddle within three guesses!Number of total times: %d times"%(time)) 
        else:
            print("Well down!You solve this riddle!Number of total times: %d times"%(time))
    else:
        print("Number of %s times: %d times"%('error',time)) 
