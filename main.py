import matplotlib.pyplot as plt
import matplotlib.ticker as plticker

sec = range(18)

fig, ax = plt.subplots()

ax.plot([-1, 18], [0, 0], color='black')  # Нулевая линия

ax.plot(sec, [])  # Высота

ax.plot(sec, [])  # Температура

ax.plot(sec, [])  # Давление

ax.plot(sec, [])  # Скорость

ax.plot(sec, [])  # Ускорение

plt.vlines(x=6, ymin=-60, ymax=250, color='black', linestyles="dashed")
plt.text(x=6, y=150, s="Апогей", ha='center', va='center', rotation='vertical', backgroundcolor='white')

plt.xlabel('Время (секунды)')
plt.legend(['Нулевая линия', 'Высота', 'Температура', 'Скорость', 'Ускорение'], loc="upper left")
ax.xaxis.set_major_locator(plticker.MultipleLocator(base=0.5))
ax.yaxis.set_major_locator(plticker.MultipleLocator(base=10))
plt.show()
