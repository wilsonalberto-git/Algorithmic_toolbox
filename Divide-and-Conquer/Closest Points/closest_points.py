# python3
from collections import namedtuple
from itertools import combinations
import sys
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


#def minimum_distance_squared(points):
# https://towardsdatascience.com/course-1-algorithmic-toolbox-part-3-divide-and-conquer-dd9022bfa2c0
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str([self.x, self.y])

def distance(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
def construct_points(x, y):
    points = []
    for i in range(len(x)):
        points.append(Point(x[i], y[i]))
    return points

def minimum_distance(x, y):
    points = construct_points(x, y)
    sorted_p_x = sorted(points, key=lambda p: p.x)

    return large_size_min_distance(sorted_p_x)

def small_size_min_distance(points):
    result = sys.maxsize
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            result = min(result, distance(points[i], points[j]))
    return result

def large_size_min_distance(p_x):
    size = len(p_x)
    half_size = int(len(p_x) / 2)

    if size <= 3:
        return small_size_min_distance(p_x)

    left_p_x = p_x[0:half_size]
    right_p_x = p_x[half_size:size]

    left_min = large_size_min_distance(left_p_x)
    right_min = large_size_min_distance(right_p_x)
    separated_min = min(left_min, right_min)

    line_l = (left_p_x[-1].x + right_p_x[0].x) / 2
    hybrid_min = compute_hybrid_min(left_p_x, right_p_x, line_l, separated_min)

    return min(separated_min, hybrid_min)

def compute_hybrid_min(left_x, right_x, line_l, wide):
    left = []
    for i in range(len(left_x)):
        if abs(left_x[i].x - line_l) <= wide:
            left.append(left_x[i])
    right = []
    for i in range(len(right_x)):
        if abs(right_x[i].x - line_l) <= wide:
            right.append(right_x[i])
    total = left + right

    total = sorted(total, key=lambda p: p.y)

    result = wide
    for i in range(len(total)):
        for j in range(i + 1, min(i + 8, len(total))):
            if abs(total[i].y - total[j].y) <= wide:
                result = min(result, distance(total[i], total[j]))

    return result


if __name__ == '__main__':
    #input_n = int(input())
    #input_points = []
    #for _ in range(input_n):
     #   x, y = map(int, input().split())
      #  input_point = Point(x, y)
       # input_points.append(input_point)
    #print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))