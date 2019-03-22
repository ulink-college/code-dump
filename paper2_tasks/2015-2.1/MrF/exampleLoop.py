hardwareTotal = 0.0
softwareTotal = 0.0

# Get sum of all values
for i in range(0,ITEMS):
    hardwareTotal = hardwareTotal + computerParts[i]                   
    softwareTotal = softwareTotal + software[i]

# Calculate the average
hwAverage = hardwareTotal / ITEMS                              #Divide by number of ITEMS
swAverage = softwareTotal / ITEMS