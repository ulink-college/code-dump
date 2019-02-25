list1 = []
list2 = []
day1=0
day2=0
var=1
while var == 1:
    print("What is the tempurture in the ",day1+1,"midday?")
    print("What is the tempurture in the ",day2+1,"midnight?")
    a = float(input())
    b = float(input())
    if a >-0.3 and a < 42:
        day1+=1
        list1.append(a)
        print("The tempurture in the middy is:",list1)
    else:
        print("There is no such high or low temperature in Guangzhou. Please check whether there is any error in the research report.")
    if b >-0.3 and b < 42:
        day2+=1
        list2.append(b)
        print("The tempurture in the midnight is:",list2)
    else:
        print("There is no such high or low temperature in Guangzhou. Please check whether there is any error in the research report.")