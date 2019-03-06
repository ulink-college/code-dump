middaytemp = []
midnighttemp = []
days = ""
temp1 = 0
temp2 = 0

for days in range(0,2):
    temp1 = int(input("midday temp:"))
    if temp1 > 50 or temp1 <-40:
        print("Invalid variables")
    else:
        middaytemp.append(temp1)

    temp2 = int(input("midnight temp:"))
    if temp2 > 50 or temp2 < -40:
        print("Invalid variables")
    else:
         midnighttemp.append(temp2)
print(middaytemp)
i = input("waht day you want to check")
print(middaytemp[i])