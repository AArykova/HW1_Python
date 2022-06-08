# Сформировать список из N членов последовательности
# Для N = 5: 1, -3, 9,-27, 81

number = int(input('Введите число - '))

def list(n):
    return [((-3)**i) for i in range(n)]

print(list(number))
