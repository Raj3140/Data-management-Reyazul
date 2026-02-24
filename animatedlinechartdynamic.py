import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

fig, ax = plt.subplots()
x_data = []
y_data = []
line, = ax.plot([], [], lw=2)

ax.set_xlim(0, 50)
ax.set_ylim(0, 100)

def update(frame):
    x_data.append(frame)
    y_data.append(random.randint(0, 100))
    
    line.set_data(x_data, y_data)
    return line,

ani = FuncAnimation(fig, update, frames=range(50), interval=200)

plt.title("Animated Line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()