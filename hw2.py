# Пользователь задает две строки.
# Определить количество вхождений одной строки в другой

from itertools import count

str_one = str(input('Введите первую строку - '))
str_two = str(input('Введите вторую строку - '))

def entry(s1, s2):
    return s2.count(s1)
print(f'Количество вхождений первой строки во вторую: {entry(str_one, str_two)}')
