def greet(fx):
    def zfx(*args,**kwargs):  #it will run without arg kwarg but will not take input in add(x,y) and throw error  whe add() is runned 
        print("start")
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