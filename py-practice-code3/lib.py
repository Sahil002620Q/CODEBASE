def search(loop,delay):
    import time
    list = ['searching   ','searching.  ','searching.. ','searching...']
    for i in range(loop):
        for j in list:
            print(f'\r{j}',end='   ')
            time.sleep(delay)
    print("\r            \r",end='')


def lineanime(list):
    import time
    list 
    
    for line in list:
        for alphabet in line:
            print(alphabet,end='',flush=True) #flush is imp as without it the compiler can collect whole output and give it at one and animation will not appear 
            time.sleep(0.2)
        print("\n",end='')   #using end=""  because by default it is print("\n", end="\n")



def clear(inp):  #hidden bug like message
    import sys
    import time

    print(inp)

    time.sleep(0.35)
    sys.stdout.write("\033[F")   # Move to previous line
    sys.stdout.write("\033[2K")  # Clear entire line
    sys.stdout.write("\r")   # Move to next line
    sys.stdout.flush()
    



ascciv = [70,117,99,107,32,89,111,117]
text = ''
for i in ascciv:
    text += chr(i)


# print("\n",end='')


def dots(text):
    import time
    import sys
    for i in range(20):
        dots = "."*(i%3)
        sys.stdout.write(f"\r{text}" + dots + "   ")
        time.sleep(0.1)
        sys.stdout.flush()
        time.sleep(0.2)
dots("starting")


if __name__ == "__main__":
    search(3,0.2)
    clear(text)
    lineanime(["hello sahil","how are you"])

#make a game which use random and file handeling it will read file containing word list using random it will replace some character with _ , user will fill the correct value , set lim like each work can use _ max 2 or 3 time # for difficult 2 easy 
#make a repo which in which a file will take input and convert it into ascci list 