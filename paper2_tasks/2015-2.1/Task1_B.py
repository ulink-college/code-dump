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

DAYS =30
middayTemp = []
midnightTemp = []

for day in range (0,3):
    middayTemp.append(float(input("Enter midday temperature: ")))
    midnightTemp.append(float(input("Enter midnight temperature: ")))
print("Miday Temps:",middayTemp)
print("Midnight Temps:",midnightTemp)




#For Testing
'''for i in range(0,5):
    total = total + middayTemp[i]
print(total)

print(sum(middayTemp))'''


