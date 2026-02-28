import time

data = [
    "Hello Sahil",
    "Welcome to Python",
    "AI journey starts now"
]

for line in data:
    for ch in line:
        print(ch, end="", flush=True)
        time.sleep(0.1)
    print()  # move to next line