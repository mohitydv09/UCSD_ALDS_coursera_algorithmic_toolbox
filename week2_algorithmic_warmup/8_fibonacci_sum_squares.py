def fibonacci_sum_squares(n):
    last=fibonacci_last(n)
    slast=fibonacci_last(n-1)
    # print(last,slast)
    multi=(last+slast)%10
    return (multi*last)%10

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

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
