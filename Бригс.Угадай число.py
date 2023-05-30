import random
num = random.randint(1, 1000)
while True:
    print('Угадайте число от 1 до 100050')
    guess = input()
    i = int(guess)
    if i == num:
        print('Правильно!')
        break
    elif i < num:
        print('Загаданное число больше')
    elif i > num:
        print('Загаданное число меньше')