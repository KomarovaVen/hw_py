# Требуется вывести все целые степени двойки (т.е. числа вида 2к), не превосходящие числа N.
n = input('Введите число больше 2 :')

while not n.isdigit():
    n = ('Введите число больше 2 :')
n = int(n)
num_degree = 1

while  num_degree <= n:
    print(num_degree)
    num_degree *= 2
