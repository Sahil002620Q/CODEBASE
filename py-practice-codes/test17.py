import random 
import time 
data = [ "do you want to roll a die "
        ,"Enter -y to proceed :"]
for line in data:
    for ch in line:
        print(ch,end="",flush=True)
        time.sleep(0.1)
    print() 


choice = input()
time.sleep(0.6)
if choice == 'y':
    x = [1,2,3,4,5,6]
    die = random.choice(x)
    print("you got ",die)

    #mixed up randomchoice and text delay 