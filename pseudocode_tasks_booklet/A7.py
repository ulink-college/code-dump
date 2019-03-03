# Input a series of positive (>=0) numbers, ended by a negative one. 
# Add up the numbers, and print the total. 
# The negative one is not to form part of the sum.

sum = 0
number = int(input("Enter number: "))
while number >= 0:
    sum = sum + number
    number = int(input("Enter number: "))
print(sum)
