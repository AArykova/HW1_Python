# Написать программу получающую набор произведений чисел от 1 до N
# Пример: пусть N = 4, тогда [1, 2, 6, 24]

from itertools import accumulate
import operator

number = int(input('Введите число - '))

def list_comp(n):
    return list(accumulate([x for x in range(1, n + 1)], operator.mul))

print(f'Набор произведений числа {number} равен - {list_comp(number)}')
 