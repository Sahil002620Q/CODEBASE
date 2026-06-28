def search(loop,delay):
    import time
    list = ['searching   ','searching.  ','searching.. ','searching...']
    for i in range(loop):
        for j in list:
            print(f'\r{j}',end='   ')
            time.sleep(delay)
    print("\r            \r",end='')
search(1,0.5)

