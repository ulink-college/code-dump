#############################################
# CIE IGCSE CS Paper 2
# June 2015 0478/21
# Sample Answer by Mr Farren

#Task 1:
# A data logger records the temperature on the roof of a school twice a day, at midday and midnight.
# Input and store the temperatures recorded for a month. You must store the temperatures in two onedimensional
# arrays, one for the midday temperatures and one for the midnight temperatures. All the
# temperatures must be validated on entry and any invalid temperatures rejected. You must decide your
# own validation rules. You may assume that there are 30 days in a month.

midday = []
midnight = []

#Function to check if the temperature is a valid float
# Uses error catching. Goes in to a loop, then tries the input code
# If any input is entered that can not be converted to a float ValueError with be thrown

class OutOfRange(Exception):
   pass

def validTemp(message):
  while True:                                           #Thie creates an infinite loop!
    try:
       temp = float(input(message))
       if temp < -5.0 or temp > 55.0:
          raise OutOfRange
    except ValueError:                                  #If ValueError occurs it will print the message and continue the loop (it's infinite!)
       print("Not an valid number! Try again.")
       continue
    except OutOfRange:
      print("That is not in range!")
    else:                                               #If no error then the value is returned and the loop breaks
       return temp
       

for i in range (0,3):                                   #Loop through the list
    midday.append(validTemp("Enter Temperature: "))     #Capture user input via validTemp function
        

print(midday)
