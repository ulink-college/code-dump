import random
var = 1
#This is creating an infinite loop as you never alter the value of var
while var == 1:
    #print the random number
    print(random.randint(1,6))
    print("Do you want to continue? ")
    a = input()
    #if no...then you go to the break. 
    #no need for an else if/else as the while loop is still active
    #you will be returned to print(random...)
    if a == "no":
        print("Goodbye")
        break       #this is the only thing allowing you out of while loop!
