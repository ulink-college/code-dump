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
day = 0

for day in range (0,DAYS):
    invalid = True
    while invalid:
        temperature = float(input("Enter midday temperature: "))   
        if temperature < -10.0:
            print("Out of range - too low")
        elif temperature > 60.0:
            print("Out of range - too high")
        else:
            middayTemp.append(temperature)
            invalid = False
    invalid = True
    while invalid:
        temperature = float(input("Enter midnight temperature: "))
        if temperature < -10.0:
            print("Out of range - too low")
        elif temperature > 60.0:
            print("Out of range - too high")
        else:
            midnightTemp.append(temperature)
            invalid = False
print("Miday Temps:",middayTemp)        # For debugging to check that values are entered
print("Midnight Temps:",midnightTemp)

#TASK 2:
#
#-------------------------

#set initial variables
middayTotal = 0.0
midnightTotal = 0.0

# Get sum of all temps
for i in range(0,DAYS):
    middayTotal = middayTotal + middayTemp[i]                   
    midnightTotal = midnightTotal + midnightTemp[i]

# Calculate the average
middayAverage = middayTotal / DAYS                              #Divide by number of days
midnightAverage = midnightTotal / DAYS

#Output results to display with suitable prompts and formatting
print("Average midday temperature: %.1f" % middayAverage)       #Produces a string output formatted with 2 decimal places
print("Average midnight temperature: %.1f" % midnightAverage)       
print(middayAverage)
print(midnightAverage)