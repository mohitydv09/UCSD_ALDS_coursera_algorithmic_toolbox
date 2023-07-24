# def fibonacci_last_digit(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current

#     return current % 10

def fibonacci_last_digit(n):
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
    print(fibonacci_last_digit(n))
