import numpy as np
import matplotlib as plt
plt.show()

x = np.arange(0,100)
y = x*2
z = x**2

# Exercise 1
# ** Follow along with these steps: **
#     ** Create a figure object called fig using plt.figure() **
#     ** Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax. **
#     ** Plot (x,y) on that axes and set the labels and titles to match the plot below:**

fig1 = plt.figure()
ax = fig1.add_axes([0, 0, 1, 1])
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')

fig1

# Exercise 2
# Create a figure object and put two axes on it, ax1 and ax2. Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively.
#** Now plot (x,y) on both axes. And call your figure object to show it.**

fig2 = plt.figure()
ax21 = fig2.add_axes([0, 0, 1, 1])
ax21.plot(x, y)
ax21.set_xlabel('x')
ax21.set_ylabel('y')
ax22 = fig2.add_axes([0.2, 0.5, 0.2, 0.2])
ax22.plot(x, y)
ax22.set_xlabel('x')
ax22.set_ylabel('y')

fig2

# Exercise 3
# ** Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]**
# ** Now use x,y, and z arrays to recreate the plot below. Notice the xlimits and y limits on the inserted plot:**

fig3 = plt.figure()
ax31 = fig3.add_axes([0,0,1,1])
ax32 = fig3.add_axes([0.2,0.5,0.4,0.4])
ax31.plot(x, z)
ax31.set_xlabel('x')
ax31.set_ylabel('z')

ax32.plot(x, y)
ax32.set_xlabel('x')
ax32.set_ylabel('y')
ax32.set_title('zoom')
ax32.set_xlim(20, 22)
ax32.set_ylim(30, 50)

fig3

# Exercise 4
# ** Use plt.subplots(nrows=1, ncols=2) to create the plot below.**
# ** Now plot (x,y) and (x,z) on the axes. Play around with the linewidth and style**
# ** See if you can resize the plot by adding the figsize() argument in plt.subplots() are copying and pasting your previous code. **

fig4, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x, y, color = 'green', lw = 15, ls = '**')
axes[1].plot(x, z, color = 'blue', lw = 3, ls = 'steps')

fig4

fig4, axes = plt.subplots(nrows=1, ncols=2, figsize = (10, 2))
axes[0].plot(x, y, color = 'green', lw = 15, ls = '**')
axes[1].plot(x, z, color = 'blue', lw = 3, ls = 'steps')

fig4
