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

# USING .append() and a seperate 'input' variable

#Define variables and constants
DAYS = 5
middayTemp = []
midnightTemp = []
temperature = 0
day = 0

for day in range (0,DAYS):
    isValid = False
    while isValid == False:
        #temperature = float(input("Enter midday temperature: "))   #Commented out to reduce screen clutter in testing!
        temperature = float(input())
        if temperature < -10.0:
            print("Out of range - too low")
        elif temperature > 60.0:
            print("Out of range - too high")
        else:
            middayTemp.append(temperature)
            isValid = True
    isValid = False
    while isValid == False:
        #temperature = float(input("Enter midnight temperature: "))     #Commented out to reduce screen clutter in testing!
        temperature = float(input())
        if temperature < -10.0:
            print("Out of range - too low")
        elif temperature > 60.0:
            print("Out of range - too high")
        else:
            midnightTemp.append(temperature)
            isValid = True
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
print("Average midday temperature: %.2f" % middayAverage)       #Produces a string output formatted with 2 decimal places
print("Average midnight temperature:", round(midnightAverage,2))       #Produces a float

a = 0
hotDays = []
#Find highest value
for i in middayTemp:
    if i > a:
        a = i
#Find the value in the list and store the index
for i in range(0,DAYS):
    if a == middayTemp[i]:
        hotDays.append(i)

if len(hotDays) > 1:
    print("The hottest days at %.1f\u00b0C" % middayTemp[hotDays[0]])
    for i in hotDays:
        print(i+1)
else:
    print("The hottest day was day %d at %.1f\u00b0C" % (hotDays[0]+1,middayTemp[hotDays[0]]))

coolDays = []
#Find highest value
for i in midnightTemp:
    if i < a:
        a = i
#Find the value in the list and store the index
for i in range(0,DAYS):
    if a == midnightTemp[i]:
        coolDays.append(i)

if len(coolDays) > 1:
    print("The coolest days at %.1f\u00b0C" % midnightTemp[coolDays[0]] )
    for i in coolDays:
        print(i+1)
else:
    print("The coolest day was day %d at %.1f\u00b0C" % (coolDays[0]+1,midnightTemp[coolDays[0]]))