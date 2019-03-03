# Input 2 values - then look at the value stored in 
# each element of # the array (100 of them) and print 
# each value that falls between the 2 input values

a = []
for n in range(0,100):
        a.append(n)

low = int(input("Enter lower value: "))
high = int(input("Enter upper value: "))
for n in range(0,100):
        if a[n] >= low and a[n] <= high:
                print(a[n])
