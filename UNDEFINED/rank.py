import random 

list = []

list.append = input("enter more names :")

x = random.choice(list)
list.remove(x)
y = random.choice(list)
list.remove(y)
z = random.choice(list)

print(f"1st : {x}\n2nd : {y}\n3rd : {z}")

#rank or position 1 == higher priority , 3 == least 