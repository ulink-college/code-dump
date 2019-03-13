ITEMS = 15
computerParts = []
software = []
for i in range(0,ITEMS): 
    isValid = False
    while isValid == False:
        part = input(" Enter required item: ")
        if part == "apple":
            print("Not a computer part!")
        else:
            computerParts.append(part)
        isValid = True
    isValid = False 
    while isValid == False:
        part = input(" Enter required item: ")
            if part == "something else":
                print("Not a computer part!")
            else:
                software.append(part)
                isValid = True
print(computerParts)
print(software)

