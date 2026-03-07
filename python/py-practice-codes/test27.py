cart = []
while True:
    print('1 add')
    print('2 remove')
    print('3 view')

    x = input('enter choice :')  #here i found a problem like we have to create a variable to take input else input will not be stored and vanish 

    if x == "1":
        item = input('enter item : ')
        cart.append(item)
    elif x == "2":
        item = input('remove item : ')
        if item in cart:
            cart.remove(item)
    elif x == "3":
        print(cart)
    else:
        break