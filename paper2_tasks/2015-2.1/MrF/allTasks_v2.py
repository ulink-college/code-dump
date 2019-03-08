#############################################
# CIE IGCSE CS Paper 2
# June 2015 0478/21
#
# Sample Answer by Mr Farren
#***Task 1:***
# A data logger records the temperature on the roof of a school twice a day, at midday and midnight.
# Input and store the temperatures recorded for a month. You must store the temperatures in two onedimensional
# arrays, one for the midday temperatures and one for the midnight temperatures. All the
# temperatures must be validated on entry and any invalid temperatures rejected. You must decide your
# own validation rules. You may assume that there are 30 days in a month.

DAYS = 5
middayTemperature = [0.0] * DAYS
midnightTemperature = [0.0] * DAYS

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
       
def averageTemp(temperatures):
   total = 0.0
   for i in range(0,DAYS):
      total = total + temperatures[i]
   tempAverage = total / DAYS
   return tempAverage

for i in range (0,DAYS):                                   #Loop through the list
    middayTemperature[i] = validTemp("Enter midday temperature: ")    #Capture user input via validTemp function
    midnightTemperature[i] = validTemp("Enter midnight temperature: ")

print("Average midday temperature: %.2f" % averageTemp(middayTemperature))       #Produces a string output formatted with 2 decimal places
print("Average midnight temperature: %.2f" % averageTemp(midnightTemperature))       #Produces a string output formatted with 2 decimal places

