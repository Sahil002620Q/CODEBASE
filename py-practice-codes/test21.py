import time
import os

fruits = ['hii']
for line in fruits:
    for ch in line:
        print(ch, end="", flush=True)
        time.sleep(0.1)
    print()

time.sleep(1)

os.system("cls")   # clears screen (Windows)

faah = ['myself sahil']
for line in faah:
    for ch in line:
        print(ch, end="", flush=True)
        time.sleep(0.1)
    print()
