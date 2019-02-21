
import patterns  as p
global types , new_types , yesorno
new_types , yesorno = "" , ""
def one_more_round():
    yesorno = str(input("do you want to run the programme again? if yes, type yes. if no, type anything except for yes :"))
    return yesorno

def entry ():
    types = str(input("please choose a pattern within triangle , square , rectangle or circle: "))
    if types == "triangle":
        p.triangle()
    elif types == "square":
        p.square()
    elif types == "circle":
        p.circle()
    elif types == "rectangle":
        p.rectangle()
    else:
        print("you might have some mistakes on your spelling. Try again if you want")
        if one_more_round() == "yes":
            entry()
        else:
            print("are you that sure you want to quit?")
        
entry()        

def new_entry():
    new_types = str(input("choose your new pattern (within triangle , rectangle , square or circle):"))
    if new_types == "triangle":
        p.triangle()
    elif new_types == "square":
        p.square()
    elif new_types == "circle":
        p.circle()
    elif new_types == "rectangle":
        p.rectangle()
    else:
        print(" you might have some mistakes on your spelling. Try again.")   
        if one_more_round() == "yes":
            entry()
        else:
            print("thank you for using")


while one_more_round() != "yes":
    print("thank you for using!")
    break
else:
    new_entry()
    