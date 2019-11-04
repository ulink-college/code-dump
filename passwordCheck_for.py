password = "password"
attempts = 0
MAX_ATTEMPTS = 3

for attempts in range(1,4):
    userPassword = input("Enter your password: ")
    if userPassword == password:
        print("Enjoy your stay!")
        break
    elif attempts != MAX_ATTEMPTS:
        print("Sorry incorrect. You have", MAX_ATTEMPTS - attempts, "attempts remaining." )
    else:
        print("Your account is now LOCKED!")