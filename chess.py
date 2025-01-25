# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.

import matplotlib.pyplot as plt
import numpy as np

data = np.array([[1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1]])

fig, ax = plt.subplots()
plt.imshow(data, cmap='hot')
plt.xticks(range(len(data)), labels=[f"{i}" for i in range(1, 9)])
plt.yticks(range(len(data)), labels=[f"{i}" for i in range(8, 0, -1)])

coordx = int(input())
cx = coordx - 1
coordy = int(input())
if coordy == 8:
    cy = 0
elif coordy == 7:
    cy = 1
elif coordy == 6:
    cy = 2
elif coordy == 5:
    cy = 3
elif coordy == 4:
    cy = 4
elif coordy == 3:
    cy = 5
elif coordy == 2:
    cy = 6
elif coordy == 1:
    cy = 7
elif coordy == 0:
    cy = 8
c = 0
for i in range(len(data)+1):
    c = plt.Circle((i, cy), 0.4, color="red", label="Окружность")
    ax.add_patch(c)
    c = plt.Circle((cx, i), 0.4, color="red", label="Окружность")
    ax.add_patch(c)
    c = plt.Circle((cx+1*i, cy+1*i), 0.4, color="red", label="Окружность")
    ax.add_patch(c)
    c = plt.Circle((cx - 1 * i, cy - 1 * i), 0.4, color="red", label="Окружность")
    ax.add_patch(c)
    c = plt.Circle((cx + 1 * i, cy - 1 * i), 0.4, color="red", label="Окружность")
    ax.add_patch(c)
    c = plt.Circle((cx - 1 * i, cy + 1 * i), 0.4, color="red", label="Окружность")
    ax.add_patch(c)

c = plt.Circle((cx, cy), 0.4, color="blue", label="Окружность")
ax.add_patch(c)

plt.show()
