# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.

import matplotlib.pyplot as plt
import numpy as np

n = 1000
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
cm1 = 0
cm2 = 0
cm3 = 0
cm4 = 0
cm5 = 0
cm6 = 0

j = np.random.randint(1, 7)

for i in range(n):
    if j == 1:
        c1+=1
    if j == 2:
        c2+=1
    if j == 3:
        c3+=1
    if j == 4:
        c4+=1
    if j == 5:
        c5+=1
    if j == 6:
        c6+=1
        
    if i == 1:
        c1+=1
        cm1+=1
    if i == 2 and i == j:
        c2+=1
        cm2+=1
    if i == 3 and i == j:
        c3+=1
        cm3+=1
    if i == 4 and i == j:
        c4+=1
        cm4+=1
    if i == 5 and i == j:
        c5+=1
        cm5+=1
    if i == 6 and i == j:
        c6+=1
        cm6+=1
    j = np.random.randint(1, 7)
    j = i

s = c1 + c2 + c3 + c4 + c5 + c6
cm = max(cm1, cm2, cm3, cm4, cm5, cm6)
print(c1, c2, c3, c4, c5, c6)
print(f"{c1/s * 100}%, {c2/s * 100}%, {c3/s * 100}%, {c4/s * 100}%, {c5/s * 100}%, {c6/s * 100}%")
print(cm)



