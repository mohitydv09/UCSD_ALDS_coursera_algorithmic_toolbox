from itertools import combinations

def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions

def merge(left,right):
    merged_arr=[]
    global count
    # print(f'Merge called for Left: {left} and right:{right}')
    #del is a O(n) operation and should be used but here I have used it for simplicity.
    while len(left)>0 and len(right)>0:
        if left[0]<=right[0]:
            merged_arr.append(left[0])
            del left[0]
        else:
            count+=len(left)
            merged_arr.append(right[0])
            del right[0]
    merged_arr.extend(left)
    merged_arr.extend(right)
    # print(f'merged returned:{merged_arr}')
    return merged_arr

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    array_left=arr[:mid]
    array_right=arr[mid:]
    # print(f"Left:{array_left} and Right:{array_right}")
    sorted_left=merge_sort(array_left)
    sorted_right=merge_sort(array_right)
    merged_arr=merge(sorted_left,sorted_right)
    return merged_arr
    
if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    global count
    count=0
    assert len(elements) == input_n
    merge_sort(elements)
    print(count)
