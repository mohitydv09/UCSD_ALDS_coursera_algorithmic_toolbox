# Uses python3
import sys

def fibonacci_partial_sum(from_, to):
    last_to=fibonacci_sum(to)
    last_from=fibonacci_sum(from_-1)
    diff=last_to-last_from
    if diff<0:
        return 10+diff
    else:
        return diff

def fibonacci_last(n):
    if n <= 1:
        return n

    list_of_mod=[0,1,1]

    while not (list_of_mod[-1]==1 and list_of_mod[-2]==0):
        add=(list_of_mod[-1]+list_of_mod[-2])%10
        list_of_mod.append(add)

    new_variable=len(list_of_mod)-2

    foo=n%new_variable

    return list_of_mod[foo]

def fibonacci_sum(n):
    last=fibonacci_last(n+2)-1
    if last==-1:
        return 9
    else:
        return last

if __name__ == '__main__':
    # input = sys.stdin.read();
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum(from_, to))
