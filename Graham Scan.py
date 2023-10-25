"""
file: Graham Scan.py
purpose: Builds a Convex Hull with given sets of points from a file using Graham Scan Algorithm
Author: Kedar Fitwe (kf3121@rit.edu)
"""


import Convexhelper as c
import time
import sys


def convex_hull(points):
    """
    Builds a Convex Hull with given sets of points using Graham Scan Algorithm
    :param points: points
    :return: A list of points that are part of the hull in a counterclockwise order
    """
    hull = []
    # Sorting done on the basis of x-coordinate and if it's a tie the on y
    points.sort(key=lambda x: [x[0], x[1]])
    first = points.pop(0)
    hull.append(first)
    # Sort the points counterclockwise w.r.t the first point
    points.sort(key=lambda p: (c.get_slope(p, first), -p[1], p[0]))

    for point in points:
        if point not in hull:
            hull.append(point)
        while len(hull) > 2 and c.check_orientation(hull[-3], hull[-2], hull[-1]) == 1:
            hull.pop(-2)

    return hull


def main():
    filename = sys.argv[1]
    points = c.get_points(filename)
    start_time = time.perf_counter()
    hull_points = convex_hull(points)
    end_time = time.perf_counter()
    print("Time : " + str(end_time-start_time))
    print("Points :", hull_points)
    c.update_points(hull_points, 'output_gs.txt')
    c.draw_plot(points, hull_points)


if __name__ == "__main__":
    main()
