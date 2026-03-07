import time
lines = ["hello",
         'myself sahil']

for line in lines :
    for ch in line :
        print(ch,end="",flush=True)
        time.sleep(0.1)
    print()