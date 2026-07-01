def greet(fx):
    def zfx(*args,**kwargs):  #it will run without arg kwarg but will not take input in add(x,y) and throw error  whe add() is runned 
        print("start")        # *arg takes all extra arguments and stores it in tupple name args while **kwargs takes all extra dict values and stores it in kwargs variable ,  * create empty tuple and store extra arguments while ** takes all arges with key and value and stores it in dict 
        fx(*args,**kwargs)
        print("end\n")
    return zfx

@greet
def hello():
    print("hello sahil")

@greet
def add(x,y):
    # scanf("enter first number",x)
    # scanf("enter second number",y)
    print(x+y)

def sub(x,y):
    print(x-y)
greet(sub)(100,1)    #if don't want to use greet before the funtion 


hello()      
add(1,3)
add(3,300)
greet(sub)(100,1)

#need to be learned deeply