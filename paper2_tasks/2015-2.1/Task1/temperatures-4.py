#############################################
# CIE IGCSE CS Paper 2
# June 2015 0478/21
#
#Task 1:
# A data logger records the temperature on the roof of a school twice a day, at midday and midnight.
# Input and store the temperatures recorded for a month. You must store the temperatures in two one dimensional
# arrays, one for the midday temperatures and one for the midnight temperatures. All the
# temperatures must be validated on entry and any invalid temperatures rejected. You must decide your
# own validation rules. You may assume that there are 30 days in a month.


#Getting Started - The task says:
# You must store the temperatures in two one dimensional arrays, one for the midday temperatures and one for the midnight temperatures.

#Create your arrays here:
middayTemperature = []
midnightTemperature = []

#Add any other variables or constants you might need:
DAYS = 3
temperature = 0.0   #variable to collect user input


# Add values to your lists
# How can you collect user input and add this to the list?
# You will need to do this 30 times for the task (when testing, try jsut doing this 2 or 3 times)

# Write the code here to ask the user for the temperature and then add this to the correct list and repeat

for i in range(0,DAYS):
    invalidData = True
    while invalidData:
        temperature = float(input("Enter midday temperature: "))
        if temperature < -10:
            print("Value out of range - too low")
        elif temperature > 60:
            print("Value out of range - too high")
        else:
            middayTemperature.append(temperature)
            invalidData = False
    invalidData = True       
    while invalidData:
        temperature = float(input("Enter midnight temperature: "))
        if temperature < -10:
            print("Value out of range - too low")
        elif temperature > 60:
            print("Value out of range - too high")
        else:
            midnightTemperature.append(temperature)
            invalidData = False

print(middayTemperature)
print(midnightTemperature)