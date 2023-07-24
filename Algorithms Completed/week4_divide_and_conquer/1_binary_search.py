def binary_search(keys,query):
    min_index=0
    max_index=len(keys)-1
    while min_index<=max_index:
        mid_index=(min_index+max_index)//2
        if keys[mid_index]==query:
            return mid_index
        elif query>keys[mid_index]:
            min_index=mid_index+1
        elif query<keys[mid_index]:
            max_index=mid_index-1
    return -1

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')