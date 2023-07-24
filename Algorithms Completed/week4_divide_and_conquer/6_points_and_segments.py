from sys import stdin
from collections import namedtuple

Segment=namedtuple('Segment','start end')

def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)
    
    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1
    return count

def binary_search_last(keys, query): #Returns last index of a query if present, otherwise give the index at which it shoudh have been
    # write your code here
    start_index=0
    end_index=len(keys)-1
    while True:
        mid_index=(start_index+end_index)//2
        if end_index-start_index<=1:
            if keys[end_index]==query:
                return end_index
            elif keys[start_index]==query:
                return start_index
            else:
                if query>keys[end_index]:
                    return end_index
                elif query>keys[start_index]:
                    return start_index
                else:
                    return start_index-1

        if keys[mid_index]==query:
            if keys[mid_index+1]!=query:
                return mid_index
            else:
                start_index=mid_index+1
        elif query>keys[mid_index]:
            start_index=mid_index+1
        elif query<keys[mid_index]:
            end_index=mid_index

def points_covered(starts,ends,points):
    starts=sorted(starts)
    ends=sorted(ends)
    counts=[]
    for point in points:
        starts_count=binary_search_last(starts,point)+1
        #in code below point-1 is passed to get the ends before that point
        ends_count=binary_search_last(ends,point-1)+1
        no_of_segments=starts_count-ends_count
        counts.append(no_of_segments)
    return counts
    
if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]
    output_count = points_covered(input_starts,input_ends,input_points)
    print(*output_count)
