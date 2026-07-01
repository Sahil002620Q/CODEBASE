def decorate(basef):
    def takeem():
        #code
        print("start")
        basef()
        #code
        print("end")
    return takeem

@decorate
def tea():
    print("tea")

tea()