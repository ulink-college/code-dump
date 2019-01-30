print("Which times table would you like?")
print("Please print here:")
n = 11
num=int(input())
counter = 0
while counter <= n:
    sum = num * counter
    print(num,"*",counter,"=",sum)
    counter += 1
   
    if counter == 11:
        break