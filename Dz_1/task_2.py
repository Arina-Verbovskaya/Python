# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
number=int(input('Введите трехзначное число: '))
sum=0
while number>0:
    sum+=number%10
    number=number//10
print(sum)


