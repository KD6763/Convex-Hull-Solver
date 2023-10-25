"""
file: RandomGenerator.py
purpose: Randomly generates points and store then in the input file for the convex hull
Author: Kedar Fitwe (kf3121@rit.edu)
"""


import random
import sys


def generate_points(n):
    """
    Randomly generate n random points
    :param n: Number of random points needed
    :return: List of generated random points
    """
    points = list()
    points.append(str(n))
    for i in range(n):
        x = str(random.randint(-len(str(n))*10, len(str(n))*10))
        y = str(random.randint(-len(str(n))*10, len(str(n))*10))
        points.append(x + " " + y)
    return points


def update_points(points):
    """
    Updates the Convex Hull points to the input file
    :param points: Randomly generated points
    """
    n = str(len(points))
    with open("input.txt", "w") as f:
        for point in points:
            f.write(point + "\n")


def main():
    n = int(sys.argv[1])
    points = generate_points(n)
    update_points(points)


if __name__ == "__main__":
    main()

