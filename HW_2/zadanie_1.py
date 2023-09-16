# На столе лежат п монеток. Некоторые из них лежат вверх решкой, а некоторые - гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть.
num = input('Введите количество монет :')
while not num.isdigit():
    print('Вы ввели не корректные числа :')
    num = ('Введите количество монет :')
num = int(num)
zeros = 0
ones = 0
for _ in range(num):
    n = input('Введите 0 или 1: ')
    while n not in ('0', '1'):
        print('Вы ввели не корректные числа :')
        n = input('Введите 0 или 1 : ')
    if n == '0':
        zeros += 1
    else:
        ones += 1
if zeros <= ones:
    print(zeros)
else:
    print(ones)