ITEMS = 5	            # A 'constant' to make things easier later on - this is set to the number of data elements/entries we require
computerParts = []
software = []			# this is jsut to show we are using a list. This creates an empty list - no data, no elements

for i in range(0,ITEMS):        #set up our for loop that runs in a 'range' of values. Start at 0, end the loop at 'ITEMS' (currently = 5)
    isValid = False             #A variable we need for our second loop
    while isValid == False:          #Our second loop so that we keep asking the user for a valid input before moving on to collecting the next item
        part = input(" Enter required item: ")  # Get input - REMEMBER the string in the brackets is a 'prompt' shown to the user. This saves us having to print() a line of text
        if part == "apple":                     #SELECTION - like asking a question. We compare 1 value to another, if it is TRUE run the code below (i.e. if user input is equal to apple...)
            print("Not a computer part!")       #Code that runs if the user enters apple
        else:		                            #The "catch-all" condition that runs when the first condition is FALSE (i.e. user enters something other than apple)
            computerParts.append(part)          #Add the value of variable 'part' to the end of the list
            isValid = True
    isValid = False             #A variable we need for our second loop
    while isValid == False:          #Our second loop so that we keep asking the user for a valid input before moving on to collecting the next item
        part = input(" Enter required item: ")  # Get input - REMEMBER the string in the brackets is a 'prompt' shown to the user. This saves us having to print() a line of text
        if part == "apple":                     #SELECTION - like asking a question. We compare 1 value to another, if it is TRUE run the code below (i.e. if user input is equal to apple...)
            print("Not a computer part!")       #Code that runs if the user enters apple
        else:		                            #The "catch-all" condition that runs when the first condition is FALSE (i.e. user enters something other than apple)
            software.append(part)          #Add the value of variable 'part' to the end of the list
            isValid = True  
                                  #This sets our 'flag' variable to TRUE so that when we return to the 'while' loop, it's condition is FALSE and this loop exits
                                                #The code returns to the outer 'for' loop and move to the next value (so long as it is not yet 5)
print(computerParts)                            #This line runs once the while loop condition is FALSE *AND* the 'for' loop has hit the upper value in the range

                                                #**NOTE*** There are other ways of writing this code and the condition isValid == False 
                                                # can be written in a slightly less confusing way. BUT this works and I wanted to show you a way to 
                                                # get started
