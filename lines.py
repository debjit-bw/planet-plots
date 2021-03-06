import matplotlib.pyplot as plt
import matplotlib.lines as mlines


def newline(p1, p2):
    ax = plt.gca()
    xmin, xmax = ax.get_xbound()

    if p2[0] == p1[0]:
        xmin = xmax = p1[0]
        ymin, ymax = ax.get_ybound()
    else:
        ymax = p1[1] + (p2[1] - p1[1]) / (p2[0] - p1[0]) * (xmax - p1[0])
        ymin = p1[1] + (p2[1] - p1[1]) / (p2[0] - p1[0]) * (xmin - p1[0])

    l = mlines.Line2D([xmin, xmax], [ymin, ymax])
    ax.add_line(l)
    return l


import numpy as np


p1 = [1, 20]
p2 = [6, 70]

newline(p1, p2)
plt.xlim(-100, 100)
plt.ylim(-100, 100)
# f = plt.figure()
# f.set_figwidth(10)
# f.set_figheight(10)

plt.savefig('trial.png', dpi=100)
plt.show()
