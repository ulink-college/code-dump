password = "changeme"
userPass = ""
count = 0

while (count <5):
    userPass = input("Enter password: ")
    count +=1
    if password == userPass:
        print("Accepted")
        #print("Attempts:",count)
        break
    
print("Attempts:",count)

