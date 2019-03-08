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

DAYS = 30
middayTemperature = []
midnightTemperature = []


#Function to check if the temperature is a valid float
# Uses error catching. Goes in to a loop, then tries the input code
# If any input is entered that can not be converted to a float ValueError with be thrown
def validTemp(message):
   while True:                                           #Thie creates an infinite loop!
      try:
         temp = float(input(message))
      except ValueError:                                  #If ValueError occurs it will print the message and continue the loop (it's infinite!)
         print("Not an valid number! Try again.")
         #continue
      else:
         if temp < -5.0:
            print("Too low")
         elif temp > 60.0:
            print("too high")
         else:                                               
            return temp                                  #If no error then the value is returned and the loop breaks
       

for i in range (0,DAYS):                                   #Loop through the list
    middayTemperature.append(validTemp("Enter midday temperature: "))     #Capture user input via validTemp function
    midnightTemperature.append(validTemp("Enter midnight temperature: "))

print(middayTemperature)
print(midnightTemperature)
