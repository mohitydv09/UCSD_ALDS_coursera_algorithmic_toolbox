from sys import stdin

def print_ans(answer):
    print("Answer")
    for x in answer:
        print(x)

def maximum_gold(capacity, weights):
    #Initialize a array to keep track of the answer
    answer=[[0 for _ in range(capacity+1)] for _ in range(len(weights)+1)]
    # print_ans(answer)

    for j in range(1,capacity+1):
        for i in range(1,len(weights)+1):
            weight_i=weights[i-1]
            if weight_i>j:
                answer[i][j]=answer[i-1][max(j,0)]
            else:
                answer[i][j]=max(answer[i-1][max(j-weight_i,0)] + weight_i, answer[i-1][max(j,0)])
    # print_ans(answer)
    return answer[len(weights)][capacity]

if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n
    # input_capacity=10
    # input_weights=[1,4,8]
    print(maximum_gold(input_capacity, input_weights))
