from collections import namedtuple
from itertools import combinations
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

def minimum_distance_squared(points):
    if len(points)<=3:
        min_distance_squared = float("inf")
        for p, q in combinations(points, 2):
            min_distance_squared = min(min_distance_squared,distance_squared(p, q))
        return min_distance_squared
    # points=sorted(points)
    n=len(points)
    first_half=points[:n//2]
    second_half=points[(n//2):]
    # print(f"First Half:{first_half}\nSecond Half:{second_half}")
    
    d1=minimum_distance_squared(first_half,)
    d2=minimum_distance_squared(second_half)
    # d1,d2=2,2
    d=min(d1,d2)
    # print("First Half",first_half[-1])
    # print("Second Half",second_half[0])
    mid_line=(first_half[-1].x + second_half[0].x)/2
    sub_strip=[point for point in points if abs(point.x-mid_line)<=d]
    # print("Sub Strip",sub_strip)
    sorted_by_y=sorted(sub_strip,key=lambda x:x[1])
    # print("Sorted by Y:",sorted_by_y)
    strip_min_dis=float('inf')
    for i in range(len(sorted_by_y)):
        for j in range(7):
            try:
                temp=distance_squared(sorted_by_y[i],sorted_by_y[i+j+1])
                # print(f'Temp:{temp}')
                if temp<strip_min_dis:
                    strip_min_dis=temp
            except IndexError:
                pass
    # print("Strip Min Dis:",strip_min_dis)
    d_final=min(strip_min_dis,d)
    return d_final

if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)
    input_points=sorted(input_points)
    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
