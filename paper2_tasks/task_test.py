#Dinesh Kumar P, IBDP Facilitator, Indus International School#
#Task 1
print("******************************Task 1 Begin******************************\n")
no_of_items=int(input("Enter the no of items:\n"))

while no_of_items<10:
    no_of_items=int(input("Invalid,Enter the no of items(minimum 10):\n"))

item_number=[0]*no_of_items
description=[None]*no_of_items
reserve_price=[0]*no_of_items
biding=[0]*no_of_items

i=0
while i<no_of_items:
    print("Item:",i)
    item_num=int(input("Enter the Item Number:\n"))
    j=0
    while j<=i:
        while item_num==item_number[j]:
            item_num=int(input("Already Exist,ReEnter the Item Number:\n"))
            j=0
        j=j+1
    item_number[i]=item_num
    description[i]=input("Enter the Description\n")
    reserve_price[i]=int(input("Enter the Reserve price\n"))
    biding[i]=0
    i=i+1
    print("i=",i)
    
    
for i in range(no_of_items):
    print ("Item Number=",item_number[i],"-",biding[i])
print("******************************Task 1 End******************************\n")
print("\n")
print("\n")
print("*****Task 2 Begin*****\n")

no_of_buyers=int(input("Enter the number of buyers\n"))
buyers_number=[0]*no_of_buyers
cur_high_bid=[0]*no_of_items
buyers_bid=[0]*no_of_items

for i in range(no_of_buyers):
    buyers_number[i]=1000+i


status="yes"
while status=="YES" or status=="yes" or status=="Y" or status=="yes":
    item_num=int(input("Enter the Item Number to bid:\n"))
    l=0
    while l==0:
        if item_num not in item_number:
            item_num=int(input("Wrong, Please Enter the valid item number\n"))
        else:
            l=1

        for i in range(no_of_items):
            if item_num==item_number[i]:
                index=i

    print("Item Number=",item_number[index],"\n")
    print("Item Number=",description[index],"\n")
    print("Item Number=",cur_high_bid[index],"\n")

    buyers_num=int(input("Enter the buyers number\n"))
    l=0

    while l==0:
        if buyers_num not in buyers_number:
            buyers_num=int(input("Wrong, Please Enter the valid buyers number\n"))
        else:
            l=1

    for i in range(no_of_buyers):
        if buyers_num==buyers_number[i]:
            index1=i

    bid_amount=int(input("Enter the bidding amount"))
    while bid_amount<=cur_high_bid[index1]:
        bid_amount=int(input("Please Enter the highest bidding amount"))
    biding[index]=biding[index]+1
    buyers_bid[index1]=buyers_bid[index1]+1
    
    status=input("Do you want to bid again:\n")