import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


x = np.linspace(0, 10, 100)
y = np.sin(x)


fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)


def init():
    line.set_data([], [])
    return line,


def update(frame):
    line.set_data(x[:frame], y[:frame])
    return line,


ani = FuncAnimation(
    fig,
    update,
    frames=len(x),
    init_func=init,
    interval=30,
    blit=True
)

plt.title("Animated Static Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()