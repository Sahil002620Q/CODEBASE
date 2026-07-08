# #up one line and clear
# import time
# import sys
# print(sys.stdout.isatty())
# print("Loading...")

# time.sleep(2)
# print("Loading...")
# time.sleep(2)

# print("\033[F\033[K",end=' ')
# # print("                 ")

import sys
import time

print("Hello")
time.sleep(1)

sys.stdout.write("\033[F")   # Move to previous line
sys.stdout.write("\033[2K")  # Clear entire line
sys.stdout.write("\033[E")   # Move to next line
sys.stdout.flush()