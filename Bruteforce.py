"""
file: Bruteforce.py
purpose: Builds a Convex Hull with given sets of points from a file using Bruteforce Algorithm
Author: Kedar Fitwe (kf3121@rit.edu)
"""


import Convexhelper as c
import time
import sys


def convex_hull(points):
    """
    Builds a Convex Hull with given sets of points using Brute Force Algorithm
    :param points: points
    :return: A list of points that are part of the hull in a counterclockwise order
    """
    n = len(points)
    if n < 3:
        return "No Convex hull possible"

    hull = []

    # Loop through all pairs of points to check their orientation with respect to the third point.
    for i in range(n):
        for j in range(n):
            valid = True
            if points[j] != points[i]:
                for k in range(n):
                    if points[k] != points[j] and points[k] != points[i]:
                        if c.check_orientation(points[i], points[j], points[k]) == 1:
                            valid = False
                            break

                # If the orientation is counterclockwise for all k, add points[i] and points[j] to the hull.
                if valid:
                    if tuple(points[i]) not in hull:
                        hull.append(tuple(points[i]))
                    if tuple(points[j]) not in hull:
                        hull.append(tuple(points[j]))

    # Sorting done on the basis of x-coordinate and if it's a tie the on y
    hull.sort(key=lambda x: [x[0], x[1]])
    first = hull.pop(0)
    # Sort the points counterclockwise w.r.t the first point
    hull.sort(key=lambda p: (c.get_slope(p, first), -p[1], p[0]))
    hull.append(first)

    return hull


def main():
    filename = sys.argv[1]
    points = c.get_points(filename)
    start_time = time.perf_counter()
    hull_points = convex_hull(points)
    end_time = time.perf_counter()
    print("Time : " + str(end_time - start_time))
    print("Points :", hull_points)
    c.update_points(hull_points, 'output_bf.txt')
    c.draw_plot(points, hull_points)


if __name__ == "__main__":
    main()
