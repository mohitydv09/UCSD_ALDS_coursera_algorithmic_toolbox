def majority_element_naive(elements):
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0

def majority_element(elements):
    if len(elements)==1:
        return 1
    elements=sorted(elements)
    mid=len(elements)//2
    possible_item=elements[mid]
    first_index,last_index=binary_search_first(elements,possible_item),binary_search_last(elements,possible_item)
    count=last_index-first_index+1
    # print(f"First:{first_index}\nLast:{last_index}")
    if count>len(elements)/2: return 1
    else: return 0

def binary_search_first(keys, query):
    # write your code here
    start_index=0
    end_index=len(keys)-1
    while True:
        mid_index=(start_index+end_index)//2
        #When ony two elements remain in the search space, we direct check for both the items.
        if end_index-start_index<=1:
            if keys[start_index]==query:
                return start_index
            elif keys[end_index]==query:
                return end_index
            else:
                return -1
        #Below we check for whether the element is first occurance or not.
        if keys[mid_index]==query:
            if keys[mid_index-1]!=query:
                return mid_index
            else:
                end_index=mid_index-1
        elif query>keys[mid_index]:
            start_index=mid_index
        elif query<keys[mid_index]:
            end_index=mid_index-1

def binary_search_last(keys, query):
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
                return -1
        
        if keys[mid_index]==query:
            if keys[mid_index+1]!=query:
                return mid_index
            else:
                start_index=mid_index+1
        elif query>keys[mid_index]:
            start_index=mid_index+1
        elif query<keys[mid_index]:
            end_index=mid_index

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
