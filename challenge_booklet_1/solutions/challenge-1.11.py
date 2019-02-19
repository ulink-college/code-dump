###############################################
#
#   1.11
#

hours = int(input("How long, on average, do you spend on a computer each day? "))

if hours < 2:
    print("That seems reasonable")
elif hours < 4:
    print("Do you have time for anything else?")
else:
    print("You need to get some fresh air once in a while, and a life!")