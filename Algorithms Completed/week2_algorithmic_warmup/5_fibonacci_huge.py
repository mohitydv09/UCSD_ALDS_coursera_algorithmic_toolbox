def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    list_of_mod=[0,1,1]

    while not (list_of_mod[-1]==1 and list_of_mod[-2]==0):
        add=(list_of_mod[-1]+list_of_mod[-2])%m
        list_of_mod.append(add)

    new_variable=len(list_of_mod)-2

    foo=n%new_variable

    return list_of_mod[foo]

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
