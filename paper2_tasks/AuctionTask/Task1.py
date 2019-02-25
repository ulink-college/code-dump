#Dinesh Kumar P, IBDP Facilitator, Indus International School#
#Task 1
print("*****Task 1 Begin*****\n")
item_number=[]
description=[]
reserve_price=[]
biding=[]

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
print("*****Task 1 End*****\n")
