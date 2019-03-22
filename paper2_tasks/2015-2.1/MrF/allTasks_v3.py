#############################################
# CIE IGCSE CS Paper 2
# June 2015 0478/21
# Sample Answer by Mr Farren
DAYS = 5
middayTemperature = [0.0] * DAYS
midnightTemperature = [0.0] * DAYS
lowTemp, highTemp = -10.0, 60.0

class TempTest:
   def __init__(self):
      self.temp = validTemp
      self.tempAverage = averageTemp
      self.x   = 
      self.hotDays

   def validTemp(self, message):
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
         
   def averageTemp(self, temperatures):                           #Function: Calculate average temperatures using a loop
      total = 0.0
      for i in range(0,DAYS):
         total = total + temperatures[i]
      tempAverage = total / DAYS
      return tempAverage

   def xTemp(self, temperatures, timeOfDay):
      if timeOfDay == "MD":
         x = lowTemp
      elif timeOfDay == "MN":
         x = highTemp
      hotDays, coolDays = [] , []
      while True:
         for i in range (0,DAYS):
            if timeOfDay == "MD":
               if temperatures[i] > x:
                  x = temperatures[i]
            elif timeOfDay == "MN":
               if temperatures[i]< x:
                  x = temperatures[i]
         for i in range(0,DAYS):
            if timeOfDay == "MD":
               if x == temperatures[i]:
                  hotDays.append(i)
            elif timeOfDay == "MN":
               if x == temperatures[i]:
                  hotDays.append(i)
         break
      return x, hotDays

mdt = TempTest
for i in range (0,DAYS):                                   #Loop through the list
    middayTemperature[i] = TempTest.validTemp("Enter midday temperature: ")    #Capture user input via validTemp function
    midnightTemperature[i] = validTemp("Enter midnight temperature: ")

print("\nAverage midday temperature: %.2f" % averageTemp(middayTemperature))       #Produces a string output formatted with 2 decimal places
print("Average midnight temperature: %.2f" % averageTemp(midnightTemperature))       #Produces a string output formatted with 2 decimal places

print(xTemp(middayTemperature, "MD"))
print(xTemp(midnightTemperature, "MN"))
print(xTemp.x)
