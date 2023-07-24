from itertools import permutations


def max_dot_product_default(first_sequence, second_sequence):
    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)
    return max_product

def max_dot_product(first_seq,second_seq):
    sorted_first_seq=sorted(first_seq)
    sorted_second_seq=sorted(second_seq)
    dot_product=0
    for i in range(len(first_seq)):
        dot_product+=sorted_first_seq[i]*sorted_second_seq[i]
    return dot_product

if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
