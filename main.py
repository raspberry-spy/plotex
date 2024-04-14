import matplotlib.pyplot as plt
import matplotlib.ticker as plticker

sec = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11.5, 12, 12.5, 13,
       13.5, 14]

fig, ax = plt.subplots()

ax.plot(sec,
        [0, 22.2796, 52.4861, 84.6056, 117.898, 146.519, 168.736, 189.324, 203.392, 213.855, 222.109, 226.57,
         229.233,
         228.409, 225.09, 219.573, 210.293, 199.481, 185.572, 170.088, 151.667, 133.509, 112.371, 87.9137, 65.6869,
         40.9764, 15.7691, 0], color='red')  # Высота
ax.plot([-1, 15], [0, 0], color='black')  # Нулевая линия
ax.plot(sec,
        [0, 50, 60, 64, 66, 57, 44, 41, 28, 20, 16, 8, 5, -1, -6, -11, -18, -21, -27, -30, -36, -36, -42, -48, -44,
         -49, -50, 0], color='green')  # Скорость
ax.plot(sec,
        [0, 98, 20, 8, 4, -18, -26, -6, -26, -16, -8, -16, -6, -12, -10, -10, -14, -6, -12, -6, -12, 0, -12, -12, 8,
         -10, -2, 50], color='blue')  # Ускорение

plt.vlines(x=6, ymin=-60, ymax=250, color='black', linestyles="dashed")
plt.text(x=6, y=150, s="Апогей", ha='center', va='center', rotation='vertical', backgroundcolor='white')

plt.xlabel('Время (секунды)')
plt.legend(['Высота', 'Нулевая линия', 'Скорость', 'Ускорение'], loc="upper left")
ax.xaxis.set_major_locator(plticker.MultipleLocator(base=0.5))
ax.yaxis.set_major_locator(plticker.MultipleLocator(base=10))
plt.show()
