
print("Enter the final score: ")
validInput = False
while not validInput:
    score = int(input())
    if score < 0 or score > 100:
        print("Must be between 0 & 100")  #Invalid range messag
    else:
        validInput = True
if score > 95:
	print("Grade = A*")
elif score >= 85:
	print("Grade = A")
elif score >= 70:
	print("Grade = B")
elif score >= 60:
	print("Grade = C")
elif score >= 50:
	print("Grade = D")
elif score >= 40:
	print("Grade = E")
else:
	print("Grade = U")
