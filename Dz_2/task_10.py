# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2


n = int(input('Введите кол-во монет : '))
count = 0
for i in range(n):
    temp = int(input())
    if temp == False:
        count += 1
print(f'Минимальное кол-во монет, кот. нужно перевернуть {count}')
