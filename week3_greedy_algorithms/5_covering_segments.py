from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

#Greedy solution where the point with most cut lines is taken
def optimal_points(segments):
    coordinates=[]
    # write your code here
    while segments:
        points = []
        for s in segments:
            points.append(s.start)
            points.append(s.end)
        points=[*set(points)]
        
        occurance=[0]*len(points)
        for i in range(len(points)):
            for j in range(len(segments)):
                if check(points[i],segments[j]):
                    occurance[i]+=1
        # print(f"Points:{points} \nOccurances:{occurance}")
        max_index=occurance.index(max(occurance))
        # print(f"Max Index:{max_index}")
        coordinates.append(points[max_index])
        segments=[segment for segment in segments if not check(points[max_index],segment)]
    return coordinates

def check(point,segment):
    if segment.start<=point and segment.end>=point:
        return 1
    else:
        return 0

#Trying to implement the same via a sorted segment method
def optimal_points_2(segments):
    coordinates=[]
    # print(f"Intial segmets:{segments}")
    while segments:
        ends=[segment.end for segment in segments] 
        point=min(ends)
        segments=[segment for segment in segments if not check(point,segment)]
        # print(f"New Segments:{segments}")
        coordinates.append(point)
    return coordinates

if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)

