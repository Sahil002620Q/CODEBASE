class ac:
    def __init__(self,name:str,ton:str,price:int):
        self.name = name
        self.ton = ton
        self.price = price

    # def info(self,name,ton,price):
    #     print("Brand : ",self.name,"\nton   : ",self.ton,"\nPrice : ",self.price)







daikin: ac = ac(name = "Daikin",ton = "four",price = 49000)
print("Brand : ",daikin.name,"\nton   : ",daikin.ton,"\nPrice : ",daikin.price)

og: ac = ac(name = "",ton = "four",price = 44000)

mitsubi : ac = ac(name = "mitsubi",ton = "four",price = 50000)

# info(og,og,four,44000)

print("=======menu==========")
# while(true):
selfx = input("enter self :")
namec = input("enter name :")
tonc = input("enter ton :")
pricec = input("enter price")
set = {

}

#template
selfx: ac = ac(namec ,tonc ,pricec )

print("Brand : ",selfx.name,"\nton   : ",selfx.ton,"\nPrice : ",selfx.price)
