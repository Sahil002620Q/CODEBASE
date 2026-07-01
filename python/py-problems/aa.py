import sys
import time
def search():
    for i in range(20):
        dots = "."*(i%3)
        sys.stdout.write("\rSearching" + dots + "   ")
        time.sleep(0.1)
        sys.stdout.flush()
        time.sleep(0.2)
search()