# Input 3 numbers, and print the biggest.

a = input("Enter 1st number: ")
b = input("Enter 2nd number: ")
c = input("Enter 3rd number: ")

if a > b:
    bigab = a
else:
    bigab = b

if c > bigab:
    print(c)
else:
    print(bigab)
