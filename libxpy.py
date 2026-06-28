def search(loop,delay):
    import time
    list = ['searching   ','searching.  ','searching.. ','searching...']
    for i in range(loop):
        for j in list:
            print(f'\r{j}',end='   ')
            time.sleep(delay)
    print("\r            \r",end='')
search(1,0.5)

def lineanime():
    import time
    list = [
        "hello sahil",
        "how are you"
        ]
    
    for line in list:
        for alphabet in line:
            print(alphabet,end='')
            time.sleep(0.2)
        print("\n",end='')   #using end=""  because by default it is print("\n", end="\n")

lineanime()