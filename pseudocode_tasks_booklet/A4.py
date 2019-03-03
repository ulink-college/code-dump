# 4-	Input 3 numbers and print either an "all 3 equal" or a "not all equal" message.

a = input("Enter 1st number: ")
b = input("Enter 2nd number: ")
c = input("Enter 3rd number: ")

if a == b and a ==c:
    print("All 3 are equal")
else:
    print("Not all equal")