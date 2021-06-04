import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
from math import sin, cos, pi


def get_positions_from_angle(angle1_in_radians, angle2_in_radians, pl1_rad, pl2_rad):
    p1_pos = [pl1_rad * cos(angle1_in_radians), pl1_rad * sin(angle1_in_radians)]
    p2_pos = [pl2_rad * cos(angle2_in_radians), pl2_rad * sin(angle2_in_radians)]

    return (p1_pos, p2_pos)


def drawline(plt, p1, p2):
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


def angle_iter(turn_increment, fr, outer_turn_angle):
    angle_now = [0, 0]
    while angle_now[1] < outer_turn_angle:
        yield angle_now
        angle_now[0] += fr * turn_increment
        angle_now[1] += turn_increment


# usable parameters:
#     outer complete turn angle
#     what fraction of outer angular velocity is inner's angular velocity
#     radii of both planets


def main(
    pl1_rad=50,
    pl2_rad=100,
    fraction=1,
    outer_turn_angle=2 * pi,
    one_round_steps=100,
    figname = "trial.png",
    linewidth = 1.0
):
    angular = angle_iter(2 * pi / one_round_steps, fraction, outer_turn_angle)

    plt.axis('square')
    plt.xlim(-pl2_rad-50, pl2_rad+50)
    plt.ylim(-pl2_rad-50, pl2_rad+50)
    i = 0
    for angle in angular:
        pos = get_positions_from_angle(angle[0], angle[1], pl1_rad, pl2_rad)
        # print(i, '\t', pos)
        # drawline(plt, pos[0], pos[1])
        plt.plot([pos[0][0], pos[1][0]], [pos[0][1], pos[1][1]], linewidth=linewidth)
        i+=1

    plt.savefig(figname, dpi=100)
    plt.show()