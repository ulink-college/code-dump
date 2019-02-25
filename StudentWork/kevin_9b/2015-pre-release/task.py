list1 = []
list2 = []
day1=0
day2=0
while True:
        print("What is the tempurture in the ",day1+1,"midday?")
        try:
                x = float(input("Please enter a number: "))
                if x >= -0.3 and x <= 42:
                        day1+=1
                        list1.append(x)
                        print("The tempurture in the midday is:",list1)
                else:
                        print("There is no such high or low temperature in Guangzhou. Please check whether there is any error in the research report.")
                average=sum(list1)/len(list1)
                print("The average value of midday is:",average,"°C")
                print("The highest tempurture of the midday is:",max(list1),"°C","The day is:",list1.index(max(list1))+1)
                print("What is the tempurture in the ",day2+1,"midnight?")
                a = float(input("Please enter a number: "))
                if a >= -0.3 and a <= 42:
                        day2+=1
                        list2.append(a)
                        print("The tempurture in the midnight is:",list2)
                else:
                        print("There is no such high or low temperature in Guangzhou. Please check whether there is any error in the research report.")
                average=sum(list2)/len(list2)
                print("The average value of midnight is:",average,"°C")
                print("The lowest tempurture of the midday is:",min(list2),"°C","The day is:",list2.index(min(list2))+1)
        except ValueError:
                print("Oops!  That was no valid number.  Try again   ")
    
