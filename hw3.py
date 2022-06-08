# Подсчитать сумму чисел в вещественном числе

number = str(input('Введите число - '))
number = number.replace('.', '')
number_list = list(number)
number_list = map(int, number_list)
summa = sum(number_list)
print(summa)
