x = []

while True:
    a = input("Enter number or type x to exit: ")
    if a == "x":
        break
    else:
        #a = round(float(a))
        #print(a)
        x.append(round(float(a)))
for i in x:
    print(i)


