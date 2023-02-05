# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint
num = int(input('Введите длину массива: '))
list = []
for i in range(1, num):
    list.append(randint(0, 5))
print(list)
x = int(input('Введите число: '))
result = list[0]
for i in list:
    if abs(i - x) < abs(result - x):
        result = i
print(result)
