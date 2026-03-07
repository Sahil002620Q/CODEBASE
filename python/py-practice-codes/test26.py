
list = input().split()

print(list)
print(min(list))
import time
lists = ['hello'
        ,'myself sahil']
list = input().split()
for line in list:
  for ch in line:
    print(ch,end='',flush=True)
    time.sleep(0.1)
  print()
# code for line animation 