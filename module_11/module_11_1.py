import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot(projection="3d")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

arg = 3

x = np.arange(-arg*np.pi, arg*np.pi, 0.5)
y = np.arange(-arg*np.pi, arg*np.pi, 0.5)
xgrid, ygrid = np.meshgrid(x, y)
zgrid = (np.sin(xgrid)) * np.sin(ygrid) / (xgrid * ygrid)

ax.plot_surface(xgrid, ygrid, zgrid, cmap = 'plasma')

plt.show()
