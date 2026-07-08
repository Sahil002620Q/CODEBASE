print("hello")
print("hello\n")
print("hello\rvasteguna")
print("hello\tsma")
print("kaput\n\tvsma\n\tkk")

print("hello\b\b\b\b\bsam")
print(99)
print("\033[k")

import time
ko = "hiiipotato"
ln = len(ko)
vr = ln*("\b")
print(ko,vr)
time.sleep(2)
print("wallah")
