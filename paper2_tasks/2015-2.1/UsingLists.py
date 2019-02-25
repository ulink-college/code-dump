import random
  
#   a list contains several elements. Each element has an index number. 
#   The numbers start at 0!!
#   in this example Apple is 0, Pizza is 1...
myFood = ["Apple","Pizza","Roast Beef","Pear"]  

# you can print a whole list:
print(myFood)

# you can select a specific item by using the index number:
#This should print pizza
print(myFood[1])

# Your list can contain any data type:
myInts = [0, 4, 5, 99, 123]
print(myInts)

myFloats = [12.2, 45.8, 909.9999, 3.14159]
print(myFloats)

myBool = [True, False, True, True, True, False]
print(myBool)

# In other languages there are lists...but there are also arrays
# python doesn't support arrays as standard (they can be used with another module)
# so it uses these lists. 
# Arrays contain data of the same type..and only the same type!
# String[] animals = { "cat", "mouse"}
# int[] rooms = {101, 102, 103}
#
# The problem with pythons lists is that the data types can not be contained
# and python will allow you to mixe data types tpgether!
# myList = ["Hi", "My name is", 122345223, 12.45]
#
# You might find this useful...but it can also cause problems
# it would be best practice to try not to do this on purpose
# try to keep lists with only one data type!


for x in myFood:
    print(x)

myFood.pop(2)
print(myFood)