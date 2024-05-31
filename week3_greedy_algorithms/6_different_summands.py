def optimal_summands(n):
    summands = []
    # write your code here
    k=int((((8*n+1)**0.5)-1)/2)
    sum_till_k_minus1=int((k*(k-1))/2)
    for i in range(k-1):
        summands.append(i+1)
    summands.append(n-sum_till_k_minus1)
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
