#############################################
# CIE IGCSE CS Paper 2
# June 2015 0478/21
#
# Sample Answer by Mr Farren
#
#Task 1:
# A data logger records the temperature on the roof of a school twice a day, at midday and midnight.
# Input and store the temperatures recorded for a month. You must store the temperatures in two onedimensional
# arrays, one for the midday temperatures and one for the midnight temperatures. All the
# temperatures must be validated on entry and any invalid temperatures rejected. You must decide your
# own validation rules. You may assume that there are 30 days in a month.

#Define variables and constants
DAYS = 5
middayTemp = []
midnightTemp = []
temperature = 0
lowTemp = -10.0
highTemp = 60.0
day = 0

for day in range (0,DAYS):
    invalid = True
    while invalid:
        try:
            temperature = float(input("Enter midday temperature: "))   
        except ValueError:
            print("Not an valid number! Try again.")
             #continue
    
            if temperature < lowTemp:
                print("Out of range - too low")
            elif temperature > highTemp:
                print("Out of range - too high")
            else:
                middayTemp.append(temperature)
                invalid = False
    invalid = True
    while invalid:
        temperature = float(input("Enter midnight temperature: "))
        if temperature < lowTemp:
            print("Out of range - too low")
        elif temperature > highTemp:
            print("Out of range - too high")
        else:
            midnightTemp.append(temperature)
            invalid = False
print("Miday Temps:",middayTemp)        # For debugging to check that values are entered
print("Midnight Temps:",midnightTemp)

#TASK 2:

middayTotal = 0.0
midnightTotal = 0.0
for i in range(0,DAYS):
    middayTotal = middayTotal + middayTemp[i]
    midnightTotal = midnightTotal + midnightTemp[i]

middayAverage = middayTotal / DAYS
midnightAverage = midnightTotal / DAYS

print("Average midday temperature:", round(middayAverage,1))       # 
print("Average midnight temperature: %.2f" % midnightAverage)  #Produces a string output formatted with 2 decimal places       

hotDays = []
coolDays = []

#Find highest value
x = lowTemp
for i in range (0,DAYS):
    if middayTemp[i] > x:
        x = middayTemp[i]

#Find the value in the list and store the index
for i in range(0,DAYS):
    if x == middayTemp[i]:
        hotDays.append(i)
if len(hotDays) > 1:
    print("The hottest days at %.1f\u00b0C" % middayTemp[hotDays[0]])
    for i in hotDays:
        print("Day",i+1)
else:
    print("The hottest day was day %d at %.1f\u00b0C" % (hotDays[0]+1,middayTemp[hotDays[0]]))

# *****

# ******
#Find lowest value
x = highTemp
for i in range(0,DAYS):
    if midnightTemp[i] < x:
        x = midnightTemp[i]
        

#Find the value in the list and store the index
for i in range(0,DAYS):
    if x == midnightTemp[i]:
        coolDays.append(i)

if len(coolDays) > 1:
    print("The coolest days at %.1f\u00b0C" % midnightTemp[coolDays[0]] )
    for i in coolDays:
        print(i+1)
else:
    print("The coolest day was day %d at %.1f\u00b0C" % (coolDays[0]+1,midnightTemp[coolDays[0]]))

