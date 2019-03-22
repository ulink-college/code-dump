#############################################
# CIE IGCSE CS Paper 2
# June 2015 0478/21
# Sample Answer by Mr Farren
DAYS = 5
middayTemperature = [0.0] * DAYS
midnightTemperature = [0.0] * DAYS
lowTemp, highTemp = -10.0, 60.0

def validTemp(message):
   while True:                                           #Thie creates an infinite loop!
      try:
         temp = float(input(message))
      except ValueError:                                  #If ValueError occurs it will print the message and continue the loop (it's infinite!)
         print("Not an valid number! Try again.")
      else:                                              #If data type is ok, check within range
         if temp < lowTemp:
            print("Too low")
         elif temp > highTemp:
            print("too high")
         else:                                               
            return temp                                  #If no error then the value is returned and the loop breaks
       
def averageTemp(temperatures):                           #Function: Calculate average temperatures using a loop
   total = 0.0
   for i in range(0,DAYS):
      total = total + temperatures[i]
   tempAverage = total / DAYS
   return tempAverage

def highLowTemps(md, mn ):
   #Find highest value
   x, y = lowTemp, highTemp
   middayTemp, midnightTemp = md, mn
   hotDays = []
   coolDays = []
   while True:
      for i in range (0,DAYS):
         if middayTemp[i] > x:
            x = middayTemp[i]
         if midnightTemp[i] < y:
            y = midnightTemp[i]
      for i in range(0,DAYS):
         if x == middayTemp[i]:
            hotDays.append(i)
         if y == midnightTemp[i]:
            coolDays.append(i)
      break
   if len(coolDays) == 1:
      print("\nThe coolest day was day %d at %.1f\u00b0C" % (coolDays[0]+1,midnightTemp[coolDays[0]]))
   else:
      print("\nThe coolest days at %.1f\u00b0C" % midnightTemp[coolDays[0]] )
      for i in coolDays:
         print(i+1)
   if len(hotDays) == 1:
      print("The hottest day was day %d at %.1f\u00b0C" % (hotDays[0]+1,middayTemp[hotDays[0]]))
   else:
      print("The hottest days were %.1f\u00b0C" % middayTemp[hotDays[0]] )
      print("They were:")
      for i in hotDays:
         print("    day",i+1)


for i in range (0,DAYS):                                   #Loop through the list
    middayTemperature[i] = validTemp("Enter midday temperature: ")    #Capture user input via validTemp function
    midnightTemperature[i] = validTemp("Enter midnight temperature: ")

print("\nAverage midday temperature: %.2f" % averageTemp(middayTemperature))       #Produces a string output formatted with 2 decimal places
print("Average midnight temperature: %.2f" % averageTemp(midnightTemperature))       #Produces a string output formatted with 2 decimal places
highLowTemps(middayTemperature,midnightTemperature)

