import time

# print("searching\rhi")
# time.sleep(1)

# print("searching.\r")
# time.sleep(1)

# print("searching..\r")
# time.sleep(1)

import os 
import sys

# list = ['searching','searching.','searching..']
list = [9,8,7,6,5,4,3,2,1]
# for j in range(10):
for i in list:
    print(f'\r{i}',end='  ')
    time.sleep(0.1)

print("\rboom")

# os.system("clear")
# print("\nboom!")