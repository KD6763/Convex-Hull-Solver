"""
file: Convexhelper.py
purpose: helper functions for building Convex hulls
Author: Kedar Fitwe (kf3121@rit.edu)
"""


import matplotlib.pyplot as plt


def get_points(filename):
    """
    Reads the points from the input file and stores in a list
    :param filename: input file name
    :return: a list of input points
    """
    points = []
    with open(filename) as f:
        for line in f:
            points.append([int(x) for x in line.rstrip().split()])

    points.pop(0)   # Removes the first element of the file from the list i.e. the number of points
    return points


def update_points(points, filename):
    """
    Updates the Convex Hull points to the output file
    :param filename: Name for the output file
    :param points: Points forming convex hull
    """
    n = str(len(points))
    with open(filename, "w") as f:
        f.write(n + "\n")
        for point in points:
            f.write(str(point[0]) + " " + str(point[1]) + "\n")


def check_orientation(p, q, r):
    """
    Determine the orientation of three points using cross product of the vectors in a 2D plane
    :param p: First Vector
    :param q: Second Vector
    :param r: Third Vector
    :return: The orientation values after the cross product
    """
    value = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if value > 0:       # Clockwise
        return 1
    elif value == 0:    # Collinear
        return 0
    else:               # Counterclockwise
        return 2


def get_slope(p, q):
    """
    Calculate the slope between two points
    :param p: First Point
    :param q: Second Point
    :return: the slope between the given two points
    """
    if p[0] == q[0]:
        return float('inf')
    else:
        return float(p[1] - q[1])/(p[0] - q[0])


def draw_plot(points, hull_points):
    """
    Draws a plot using matplotlib, plotting all the points and joining the points forming the convex hull
    :param points: All the points available
    :param hull_points: Points forming the Convex Hull
    """
    x_points = [x[0] for x in points]
    y_points = [x[1] for x in points]
    x_hull = [x[0] for x in hull_points]
    y_hull = [x[1] for x in hull_points]
    x_hull.append(x_hull[0])
    y_hull.append(y_hull[0])
    plt.scatter(x_points, y_points)
    if len(x_points) <= 500:
        for i_x, i_y in zip(x_hull, y_hull):
            plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
    plt.plot(x_hull, y_hull, color="black")
    plt.show()
