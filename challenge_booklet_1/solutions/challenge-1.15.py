
password = "changeme"
userPass = ""
count = 0
while (password != userPass):
    userPass = input("Enter password: ")
    count +=1

print("Accepted")
print("Attempts:",count)