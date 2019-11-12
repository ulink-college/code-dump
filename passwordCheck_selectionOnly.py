password = "password"
attempts = 0
MAX_ATTEMPTS = 3

userPassword = input("Enter your password: ")
attempts += 1
if userPassword == password:
    print("Enjoy your stay!")
elif userPassword != password:
    print("Sorry incorrect. You have", MAX_ATTEMPTS - attempts, "attempts remaining." )
    userPassword = input("Enter your password: ")
    attempts += 1
    if userPassword == password:
        print("Enjoy your stay!")
    elif userPassword != password:
        print("Sorry incorrect. You have", MAX_ATTEMPTS - attempts, "attempts remaining." )
        userPassword = input("Enter your password: ")
        attempts += 1
        if userPassword == password:
            print("Enjoy your stay!")
        elif userPassword != password:
            print("Sorry incorrect. You have", MAX_ATTEMPTS - attempts, "attempts remaining." )
            print("Your account is now LOCKED!")