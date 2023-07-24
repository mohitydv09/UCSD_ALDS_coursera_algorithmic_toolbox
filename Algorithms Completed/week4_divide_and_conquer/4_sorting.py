from random import randint

def partition3(array, left, right):
    # write your code here
    pivot=array[left]
    j=left
    m=left
    # print(f'Partition recieved array:{array[left:right+1]}')
    for i in range(left+1,right+1):
        if array[i]<pivot:
            j+=1
            m+=1
            if m==j:
                # print(f"As no ele equal to pivot has been found yet.")
                array[i],array[j]=array[j],array[i]
            else:
                array[i],array[j],array[m]=array[m],array[i],array[j]
            # print(f"i:{i},j:{j},m:{m}")
            # print(f'Swaped as ele is less than pivot. New array:{array}')
        elif array[i]==pivot:
            m+=1
            array[i],array[m]=array[m],array[i]
    array[left],array[j]=array[j],array[left]
    # print(f'Partitioned array:       {array} with Pivot:{pivot}')
    # print(f"Partitioned returned: j:{j}, m{m}")
    return j,m

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1,m2= partition3(array, left, right)
    randomized_quick_sort(array, left, m1-1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
