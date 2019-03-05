day = int(input("how many days would you like to record?"))
times = int(input("how many times would you like to record for each MDN and MDD"))
midday = [None]*day*times
midnight = [None]*day*times
i = 0
days = 0
while(i<day*2):
    h=0
    while(h<times):
        print("day",days+1,"the attempts",h+1,"midday")
        midday[i]=int(input("please type midday's temperature here (you must tpye a number)"))
        if (midday[i]<=60)and(midday[i]>=-10):
            i+=1
            h+=1
        else:
            print("**************out of range**************")
    i-=times
    n=0
    while(n<times):
        print("day",days+1,"the attempts",n+1,"midnight")
        midnight[i]=int(input("please type midnight' temperature here (you must tpye a number)"))
        if (midnight[i]<=60) and (midnight[i]>=-10):
           i+=1
           n+=1
        else:
            print("**************out of range**************")
    days +=1
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
