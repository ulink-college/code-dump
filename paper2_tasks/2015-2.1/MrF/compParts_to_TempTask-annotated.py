# TASK - This code will *almost* work for task 1.
# It requires some changes...and a few additions....can you see where?

# TODO:
# 1. Change CONSTANT to "days"
# 2. Change the list names to somethign suitable for task 1
#       Read task 1 again and see if you can identify some sensible names for these lists
# 3. 


ITEMS = 3                              #This is just a 'constant' used to store a value - in this case it is the number of items we will store
hardwareCost = []                       # This is a list this will store costs of items
hardwareItem = []                       # This is another list, this will store text descriptors of items

#Start looping:                         #Set up our loop so we can collect ITEMS number of data  
for i in range(0,ITEMS):                #i is an 'iterator' variable. It holds the number of the loop we are running. 
                                        # These numbers come from the 'in range' function - in range(start number, exit number)
    isValid = False                     # a simple 'flag' variable
    while isValid == False:             #ANOTHER loop - this time the code inside with run 'while' the condition is true (so...whilst isValid equals false....run the code)
        part = input(" Enter hardware item: ")  #get input and store in a (temporary) variable
        if part == "":                          #this list is using strings...this lines says: if the string is empty("")....
            print("Can not be blank!")              # ...RUN this code!
        else:                                   #Otherwise (else) the string is not empty
            hardwareItem.append(part)               # ...run THIS code
            isValid = True                             # chnge the flag so that the while loop exits as we have a valid response!
    isValid = False                         # do all that again...to collect data for the second list!!
    while isValid == False:
        part = float(input(" Enter item price: "))
        if part <= 0:                          # Difference here is that we are working with numbers, so we can see if the input is less than a certain number
            print("INVALID NUMBER")
        elif part > 9999:                       #...or higher than another number!
            print("We do not have anything that expensive!")
        else:
            hardwareCost.append(part)
            isValid = True
print(hardwareCost)                             #This just prints the lists so we can see it has worked!!
print(hardwareItem) 