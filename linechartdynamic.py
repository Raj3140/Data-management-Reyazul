import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random


fig, ax = plt.subplots()

x_data = []
y_data = []

line, = ax.plot([], [], lw=2)

ax.set_xlim(0, 20)
ax.set_ylim(0, 100)

def update(frame):
    x_data.append(frame)
    y_data.append(random.randint(0, 100))
    
    line.set_data(x_data, y_data)
    

    if frame > 20:
        ax.set_xlim(frame-20, frame)
    
    return line,

ani = FuncAnimation(fig, update, interval=500)

plt.title("Dynamic Line Chart (Live Updating)")
plt.xlabel("Time")
plt.ylabel("Value")

plt.show()