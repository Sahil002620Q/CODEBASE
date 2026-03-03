cart = []

while True:
    print("1. Add item")
    print("2. Remove item")
    print("3. Show cart")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item: ")
        cart.append(item)

    elif choice == "2":
        item = input("Remove item: ")
        if item in cart:
            cart.remove(item)

    elif choice == "3":
        print(cart)

    elif choice == "4":
        break