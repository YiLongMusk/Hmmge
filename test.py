from util import arrange
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from matplotlib import pylab

x, y = arrange()
fig, ax = plt.subplots()
ax.plot(x,y)
loc = plticker.MultipleLocator(base = 5)
ax.xaxis.set_major_locator(loc)
fig = pylab.gcf()
fig.canvas.set_window_title('Setting up window title.')
plt.grid()
plt.show()
