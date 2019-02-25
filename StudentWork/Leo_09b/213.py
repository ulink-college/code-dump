B =""
times =0
import random
A = random.randint(1,3)
if A ==1:
    F ="Mississippi"
elif A ==2:
    F ="Silence"
elif A ==3:
    F ="Footsteps"
while B != F:
    times =times + 1
    if A ==1:
        B = input("What has four eyes but can not see: ")
    if A ==2:
        B = input("What will break when you say its name: ")
    if A ==3:
        B = input("The more you take, the more you leave behind. What are they: ")
if B == F and times <=3:
    print("correct, you tried "+ str(times) + " times")
if B == F and times >3:
    print("correct, you tried "+ str(times) + " times")
