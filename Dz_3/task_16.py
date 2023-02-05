# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

from random import randint
num = int(input('Введите длину массива: '))
list = []
for i in range(1, num):
    list.append(randint(0, 5))
print(list)
x = int(input('Введите искомое число: '))
count = 0
for i in range(len(list)):
    if x == list[i]:
        count += 1
print(count)