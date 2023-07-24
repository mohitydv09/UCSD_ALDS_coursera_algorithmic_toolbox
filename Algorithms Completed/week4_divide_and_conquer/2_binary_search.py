def binary_search(keys, query):
    # write your code here
    start_index=0
    end_index=len(keys)-1
    while True:
        mid_index=(start_index+end_index)//2
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
            # print(f"Query is greater then middle element.")
            start_index=mid_index
            # print(f"New start index:{start_index}")
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
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search_last(input_keys, q), end=' ')
