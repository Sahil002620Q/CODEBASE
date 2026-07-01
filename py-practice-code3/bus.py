# list 
# tuple
# set 
# dict

# needed
# seat 1 to 10

# flow user book seat it will selected randomly betwwn 1 to 20 and if it already exist it will chenge random val till got frozenset
# from lib import search, lineanime
                                      

seat = {}  #empty set


for i in range(20):
    seat[i] = {
        "name" : 'null',
        "status" : True
    }

print(seat)
# for sno in seat:
#     print(sno)

# print(seat['1']['status'])

print("---BUS STIMULTOR---")
print("1. chech status")
print("1. book")
print("1. cancel")

choice = int(input("enter choice :"))

loop = True

while(loop is True):
    if choice is 1:
        print("available seat")
        # search(3,0.4)
        for i in seat:
            if seat[i]["name"] == "null" and seat[i]["status"] == True:
            #    for i in range(20)
                print(f"Seat number {i} status : Available ")
            

            else:

                print(f"Seat number {i} status : Not Available ")
        
    # if choice is 2:
    # if choice is 3:
    if choice is 4:
        
        loop = False