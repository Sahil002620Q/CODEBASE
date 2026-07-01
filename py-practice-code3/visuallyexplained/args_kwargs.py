def tea(type,sugar_lv,price):
    print(f"user buyed {type} tea \npreffered sugar lv in tea : {sugar_lv}\nTotal price (in dollar) : {price}")

tea('matcha',"high",5)
import os 

def teax(uname,ch,type_):
    '''so if user buy , it might be tea or coffe
    need name
    need tea or coffee

    assume coffe
    need type ie latte caputino
    fix price for base coffe , fix price for type ie +40 for latte +90 for caputine
    need choice maybe extra sugar or no etc (will be free aditive)
    need additives , extra coffe powder , 

    for bill need name and total price 

    '''


    type_coffee = ["Espresso","Americano","Cappuccino","Latte","Flat White","Macchiato","Mocha","Cortado","Affogato","Ristretto","Lungo","Irish Coffee"," Cold Brew Coffee","Iced Coffee","French Press Coffee","Pour-over Coffee","Drip Coffee","Turkish Coffee","South Indian Filter Coffee","Instant Coffee"]

    bev = type_tea + type_coffee
    
    
print("enter name :",end='')
uname = input()
print("\r" + " "*50 + "\r",end='')
os.system("clear")
ch = input("1. Tea\n2. Coffee\nchoose your beverage tea or coffee :")

if ch ==1:
     #teaorcoffe[]
    input("select type : ") 
    type_tea = ["Black Tea","Green Tea","White Tea","Oolong Tea","Pu-erh Tea","Yellow Tea","Masala Chai","Ginger Tea","Elaichi Tea","Lemon Tea","Tulsi Tea","Chamomile Tea","Peppermint Tea","Hibiscus Tea","Jasmine Tea","Earl Grey Tea","English Breakfast Tea","Darjeeling Tea","Assam Tea","Kashmiri Kahwa"]


if ch ==2:
     #teaorcoffe[]
    input("select type : ")
    type_coffee = ["Espresso","Americano","Cappuccino","Latte","Flat White","Macchiato","Mocha","Cortado","Affogato","Ristretto","Lungo","Irish Coffee"," Cold Brew Coffee","Iced Coffee","French Press Coffee","Pour-over Coffee","Drip Coffee","Turkish Coffee","South Indian Filter Coffee","Instant Coffee"]
    print("Espresso")
print("1. Instant Coffee")
print("2. Cappuccino")
print("3. Latte")
print("4. Flat White")
print("5. Macchiato")
print("6. Mocha")
print("7. Cortado")
print("8. Affogato")
print("9. Ristretto")
print("10. Lungo")
print("11. Irish Coffee")
print("12. Cold Brew Coffee")
print("13. Iced Coffee")
print("14. French Press Coffee")
print("15. Pour-over Coffee")
print("16. Drip Coffee")
print("17. Turkish Coffee")
print("18. South Indian Filter Coffee")
print("19. Americano")
xch = input("enter your choice :")

def bill():
    print()




