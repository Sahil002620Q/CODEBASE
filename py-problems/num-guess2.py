import random
x = random.randint(1,10)
guess = int(input('make a guess : '))

while True:
    if guess < x:
        print('small')
        guess = int(input('make another guess'))

    elif guess > x:
        print('large')
        guess = int(input('make another guess'))

    elif guess == x:
        print('you guessed right')
        break

print(x)