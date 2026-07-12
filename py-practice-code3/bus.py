# list 
# tuple
# set 
# dict

# needed
# seat 1 to 10

# flow user book seat it will selected randomly betwwn 1 to 20 and if it already exist it will chenge random val till got frozenset
# from lib import search, lineanime
                                      
import os ,sys
seat = {}  #empty set

#seat declared
for i in range(20):
    seat[i] = {
        "name" : 'null',
        "status" : True
    }

print(seat)   
print() 
print()   
print(seat[5])                                   # for sno in seat: #     print(sno) # print(seat['1']['status'])

#menu loop

while(True):
    # os.system("clear")
    print("---BUS STIMULTOR---")
    print("1. chech status")
    print("1. book")
    print("1. cancel")
    choice = int(input("enter choice :"))
    if choice is 1:
        # os.system("clear")
        print("------available seat------")
        # search(3,0.4)
        for i in seat:
            if seat[i]["name"] == "null" and seat[i]["status"] == True:
            #    for i in range(20)
                print(f"Seat number {i} status : Available ")
            

            else:

                print(f"Seat number {i} status : Not Available ")
        input("Press enter to continue...")
        
    if choice is 2:
        print("book seat")
        namet = input("Enter your name :")
        seatt = input("Enter seat number you want to book :")
        #seat 5
        seatt = i
        print(seat[i]["name"])

        if seat[i] == seat["name"] == 'null' & seat["status"] == True:
            print("working")
        # for x in seat:
        #     if (seat["name"] == 'null' & seat["status"] == True):
        #         print("free")




    # if choice is 3:
    if choice is 4:
        
        exit()
    