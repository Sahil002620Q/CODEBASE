import winsound
import time

# Countdown beep
for i in range(5, 0, -1):
    print(i)
    winsound.Beep(800, 150)
    time.sleep(1)

print("0")

# 💥 BOOM effect (low dropping frequencies)
winsound.Beep(400, 200)
winsound.Beep(300, 200)
winsound.Beep(200, 400)

print("💥 BOOM!")