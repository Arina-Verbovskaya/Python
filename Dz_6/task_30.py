# Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input("Первый элемент: "))
d = int(input("Шаг: "))
n = int(input("Кол-во элементов: "))
for i in range(n):
    print(a+i*d)
