import random
var = "yes"
while var == "yes":
    print(random.randint(1,6))
    print("Do you want to continue? ")
    var = input()
     #entering no will change var so after the "if" var == no 
     #and the loop exits (having printed goodbye)
    if var == "no":    
        print("Goodbye")
    #if you enter yes...it keeps var == yes so the loop continues

    #here you would also have something to ensure only yes or no are entered...otherwise
    #entering "asdew" will also exit the loop!