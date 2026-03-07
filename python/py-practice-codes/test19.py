import time
import sys

# Print first line
text = ['hello']
for line in text :
    for ch in line :
        print(ch, end="", flush=True)
        time.sleep(0.1)

# Clear it (overwrite with spaces)
sys.stdout.write("\r" + " " * 20)
sys.stdout.flush()

text = ['hello']
for line in text :
    for ch in line :
        sys.stdout.write(ch,end="\r",flush=True)
        
        sys.stdout.flush()
        print(ch, end="", flush=True)
        time.sleep(0.1)

# Move back again and print new line
