day = int(input("how many days would you like to record?"))
times = int(input("how many times would you like to record for each MDN and MDD"))
midday = [None]*day*times
midnight = midday.copy()
i = 0
days = 0
date = 0
while(i<times*day):
    h=0
    while(h<times*day):
        if(days % times ==0):
            date+=1
        print("day",date,"the attempts",days+1,"midday")
        midday[i]=int(input("please type midday's temperature here (you must type a number)"))
        if (midday[i]<=60)and(midday[i]>=-10):
            i+=1
            h+=1
        else:
            print("**************out of range**************")
            print("type your data of yesterday again please(type again if this is the very first time you recored)")
            days-=1
            if(i==0):
                break
        i -= 1
        print("day",date,"the attempts",days+1,"midnight")
        midnight[i]=int(input("please type midnight' temperature here (you must type a number)"))
        if (midnight[i]<=60) and (midnight[i]>=-10):
           i+=1
           h+=1
        else:
            print("**************out of range**************")
            i+=1
            print("type your data of today again please")
            days-=1
        days += 1
L=0
for a in range(0,day,1):
    print("in the day",a+1,"midday temperature are")
    while(L<=times*day):
        print(midday[L])
        L+=1
        if (L%times==0):
            break
M=0
for u in range(0,day,1):
    print("in the day",u+1,"midnight temperature are")
    while(M<=times*day):
        print(midnight[M])
        M+=1
        if (M%times == 0):
            break
