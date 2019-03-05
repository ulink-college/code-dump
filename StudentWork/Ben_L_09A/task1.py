day = int(input("how many days would you like to record?"))
days = [None]*day*2
temperature = 0
i = 0
p=1
while(i<day*2):
        print("day",p)
        days[i]=int(input("please type midday's temperature here (you must tpye a number)"))
        if (days[i]<=60)and(days[i]>=-10):
            i+=1
        else:
            print("**************out of range**************")
        print("day",p)
        days[i]=int(input("please type midnight' temperature here (you must tpye a number)"))
        if (days[i]<=60) and (days[i]>=-10):
           i+=1
        else:
            print("**************out of range**************")
        p+=1
c=0
for a in range(0,day*2,2):
    c+=1
    print("in day",c,"temperature in middayis",days[a],"   ","temperature in midnight is",days[a+1])
