from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))
    largest = 0
    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))
    return largest

def largest_number(numbers):
    numbers=list(map(str,numbers))
    salary=''
    while numbers:
        max_number='0'
        for number in numbers:
            # if int(number)>=max_number:
            if is_better(number,max_number):
                max_number=number
                # print("New Max number:",max_number)
        salary+=max_number
        numbers.remove(max_number)
    return salary

def is_better(number,max_number):
    l=[number,max_number]
    l2=[max_number,number]
    if int("".join(l))>int("".join(l2)):
        return True
    else: return False
    
if __name__ == '__main__':
    # _ = int(input())
    # input_numbers = input().split()
    input_numbers=[21,2,23,5]
    print(largest_number(input_numbers))
