import time 
data = [ "hello",
        "sahil",
        "wassup"]

for line in data:
  for ch in line:
    print(ch, end="",flush=True)
    time.sleep(0.1)
  print() #new line for list loop