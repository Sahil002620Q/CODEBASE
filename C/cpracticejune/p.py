import time
import random
x = random.randint(1,10)
time.sleep(x)
print("hello",x)
y = input("negative time :")

if y >= x :
    time.sleep(x-y)
    print(x-y)
else :
    print("exceeded by :",y-x)