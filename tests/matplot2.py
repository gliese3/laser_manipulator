
import matplotlib.pyplot as plt
import numpy as np
import time
from random import randint
import random
import matplotlib.animation as animation



figure1, ax1 = plt.subplots()
ax1.set_axis_off()
ar1 = np.random.randint(0, 100, size = (1000, 1000))
line1 = ax1.imshow(ar1, cmap="jet", extent=[0,100,0,100], interpolation="None")
figure1.colorbar(line1)

start = time.time()

def animate(i):

    if i % 2 == 0:
        z = np.random.randint(0, 100, size = (1000, 1000))

        line1.set_clim(0, 500)
        # cbar.update_normal(line)
        # cbar.update_ticks()

    else:
        z = np.random.randint(0, 200, size = (500, 500))
        line1.set_clim(0, 200)
        # cbar.update_normal(line)
        # cbar.update_ticks()
        line1.set_data(z)

    if i == 9:
        print((time.time() - start))

    return line1,


anim = animation.FuncAnimation(figure1, animate,
                               frames=10, interval=1000, blit=True, repeat=False)