import winsound
import time

# Shock crack (sudden high impact)
winsound.Beep(2000, 40)
winsound.Beep(1500, 60)

# Fast chaotic burst
winsound.Beep(1800, 40)
winsound.Beep(1300, 50)
winsound.Beep(900, 70)

# Heavy impact pulses
winsound.Beep(800, 100)
winsound.Beep(700, 120)
winsound.Beep(600, 140)

# Final aggressive vibration
for _ in range(2):
    winsound.Beep(1000, 60)
    winsound.Beep(750, 60)

print("💥 BOOOOM 💥")