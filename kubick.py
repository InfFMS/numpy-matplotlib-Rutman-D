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
cm = 0
str = []
i = np.random.randint(1, 7)
j = 1
while j <= 1000:
    while i == 1:
        c1 += 1
        i = np.random.randint(1, 7)
        j += 1
        if i != 1:
            break
        cm += 1
    str.append(cm)
    cm = 0
    while i == 2:
        c2 += 1
        i = np.random.randint(1, 7)
        j += 1
        if i != 2:
            break
        cm += 1
    str.append(cm)
    cm = 0
    while i == 3:
        c3 += 1
        i = np.random.randint(1, 7)
        j += 1
        if i != 3:
            break
        cm += 1
    str.append(cm)
    cm = 0
    while i == 4:
        c4 += 1
        i = np.random.randint(1, 7)
        j += 1
        if i != 4:
            break
        cm += 1
    str.append(cm)
    cm = 0
    while i == 5:
        c5 += 1
        i = np.random.randint(1, 7)
        j += 1
        if i != 5:
            break
        cm += 1
    str.append(cm)
    cm = 0
    while i == 6:
        c6 += 1
        i = np.random.randint(1, 7)
        j += 1
        if i != 6:
            break
        cm += 1
    str.append(cm)
    cm = 0



s = c1 + c2 + c3 + c4 + c5 + c6
c = max(str)
print(c1, c2, c3, c4, c5, c6)
print(f"{c1 / s * 100}%, {c2 / s * 100}%, {c3 / s * 100}%, {c4 / s * 100}%, {c5 / s * 100}%, {c6 / s * 100}%")
print(c)

categories = ["1", "2", "3", "4", "5", "6"]
values = [c1 / s * 100, c2/ s * 100, c3/ s * 100, c4/ s * 100, c5/ s * 100, c6/ s * 100]

plt.bar(categories, values, color='purple')
plt.title("Столбчатая диаграмма")
plt.show()
