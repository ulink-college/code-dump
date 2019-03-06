# Totaling values
print('''
**************************
Totalling using sum()
**************************''')
myNumbers = [6,1,3,2,3,2,1,5,4,5,1,1]
print("List Content:",myNumbers)
print("Total:",sum(myNumbers))

# Totalling using a loop
print('''
**************************
Totalling using a loop
**************************
''')
listTotal = 0
for i in myNumbers:
    listTotal = listTotal + i
print("Total:",listTotal)

print('''
**************************
Totalling by adding individual elements:

Q: What problems might there be if chosing this method?
**************************
''')
print("e.g myNumbers[0] + myNumbers[1] + myNumbers[2] + ....etc")
listTotal = myNumbers[0]+myNumbers[1]+myNumbers[2]+myNumbers[3]+myNumbers[4]
print(listTotal)

print('''
**************************
Finding average using average function
**************************
''')
#Averages:
average = sum(myNumbers) / len(myNumbers)  # len() - calculates the length of an object. For a list...the number of elements it holds
print("Average:",average)

print('''
**************************
Finding largest and smallest using a max/min functions
**************************
''')
#Largest Value
print("Largest:",max(myNumbers))
#smallest value
print("Smallest:",min(myNumbers))

print('''
**************************
Finding largest and smallest using a sort
**************************
''')

sortedList = myNumbers.copy()        #This is to keep the original list unchanged so it can be used later (might be useful)
sortedList.sort()                    #Sort the new list in numeric order
print("Largest:",sortedList[-1])     #selects last value
print("Smallest:",sortedList[0])


a = 0
for i in myNumbers:
    if i > a:
        a = i
print("Largest",a)