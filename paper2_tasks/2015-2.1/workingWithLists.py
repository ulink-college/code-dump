#####################################################
#
#   Working with python lists
#
#
import random
i = random.randint(0,3)
myFood = ["Apple","Pizza","Roast Beef","Pear"]
userAnswer = ""



while userAnswer not in myFood:
    userAnswer = input("Pick a food: ")
    if userAnswer not in myFood:
        print("NOPE!")
    else:
        print("good choice")



