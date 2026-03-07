import time
import winsound

for i in range(5, 0, -1):
    print(i)
    winsound.Beep(800, 200)   # Same beep for digits
    time.sleep(1)

print(0)
winsound.Beep(1500, 700)     # Different beep at 0