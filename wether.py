# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
import random

import matplotlib.pyplot as plt
import numpy as np
arr = np.array([random.randint(-10, 35) for i in range(365)])
print(sum(arr)/len(arr))

c = 0

for i in range(len(arr)):
    if arr[i] > 25:
        c+=1
print(c)

i = 0
c1 = 0
str = []
cm = 0
while i < 365:
    while arr[i] < 0:
        i+=1
        if arr[i] >= 0:
            break
        cm += 1
    str.append(cm)
    cm = 0
    i += 1

print(max(str))
print(arr)