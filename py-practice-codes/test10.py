import sys
import time
import winsound

delay = 1.0

for i in range(5, 0, -1):
    sys.stdout.write(f"\r⏳ {i} ")
    sys.stdout.flush()
    
    winsound.Beep(1150, 80)  # sharp metallic tick
    time.sleep(delay)
    
    delay *= 0.6  # ticking speeds up

# Show 0
sys.stdout.write("\r💣 0 ")
sys.stdout.flush()

# Explosion sound (descending frequencies)
winsound.Beep(700, 100)
winsound.Beep(500, 200)
winsound.Beep(300, 400)
winsound.Beep(120, 900)

# Flash effect
for _ in range(3):
    sys.stdout.write("\r💥 BOOM!!! ")
    sys.stdout.flush()
    time.sleep(0.2)
    sys.stdout.write("\r           ")
    sys.stdout.flush()
    time.sleep(0.2)

print("\n🔥 System Destroyed")