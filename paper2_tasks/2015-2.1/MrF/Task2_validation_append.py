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
DAYS =3
middayTemp = []
midnightTemp = []
temperature = 0
day = 0

for day in range (0,DAYS):
    isValid = False
    while isValid == False:
        temperature = float(input("Enter midday temperature: "))
        if temperature < -10.0:
            print("Out of range - too low")
        elif temperature > 60.0:
            print("Out of range - too high")
        else:
            middayTemp.append(temperature)
            isValid = True
    isValid = False
    while isValid == False:
        temperature = float(input("Enter midnight temperature: "))
        if temperature < -10.0:
            print("Out of range - too low")
        elif temperature > 60.0:
            print("Out of range - too high")
        else:
            midnightTemp.append(temperature)
            isValid = True
print("Miday Temps:",middayTemp)        # For debugging to check that values are entered
print("Midnight Temps:",midnightTemp)

middayAverage = 0.0
midnightAverage = 0.0

middayAverage = sum(middayTemp)/len(middayTemp)
midnightAverage = sum(midnightTemp)/len(midnightTemp)

print("Average midday temperature: %.2f" % middayAverage)       #Produces a string output formatted with 2 decimal places
#print("Average midday temperature:", round(middayAverage,2))       #Produces a float

print("Average midnight temperature:", round(midnightAverage,2))       #Produces a float



#For Testing
middayTotal = 0.0
midnightTotal = 0.0

for i in range(0,DAYS):
    middayTotal = middayTotal + middayTemp[i]
    midnightTotal = midnightTotal + midnightTemp[i]
middayAverage = middayTotal / DAYS
midnightAverage = midnightTotal / DAYS
print(round(middayAverage,2))
print(round(midnightAverage,2))




