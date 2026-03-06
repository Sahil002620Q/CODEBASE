x = int(input('enter first number : '))
y = int(input('enter second number : '))
z = int(input('enter third number : '))

if x >= y and x >= z :
    print(f'{x} is greater')     # used >= then > as if x = 3,y =3
elif y >= x and y >= z :
    print(f'{y} is greater')
elif z >= y and z >= x :
    print(f'{z} is greater')