days = (30)
midday_temp = []
midnight_temp = []
n = 0
m = 0
while n <= days :
    MDT = int(input("input the midday temperature"))
    if MDT <= -20 or MDT >= 50:
        print("滚你妈的")
        break
    else:
        midday_temp.append(MDT)
        n = n+1
else:
    print("let's record midnight_temp")
 
    while m <= days:
        MNT = int(input("input the midnight temperature"))
        if MNT <= -20 or MDT >= 50:
           print("你是智障吗？")
           break
        else:
           midnight_temp.append(MNT)
           m = m+1
    else:
        print(midday_temp)
        print(midnight_temp)