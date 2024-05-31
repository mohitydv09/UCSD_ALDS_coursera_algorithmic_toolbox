def print_answer(answer):
    print("Answer:")
    for x in answer:
        # print(x)
        for y in x:
            print(y)
        print('\n')
        
def lcs3(first, second, third):
    #answer initiallized
    answer=[[[0]*(len(first)+1) for _ in range(len(second)+1)] for _2 in range(len(third)+1)]
    # print_answer(answer)

    for k in range(1,len(third)+1):
        for j in range(1,len(second)+1):
            for i in range(1,len(first)+1):
                if first[i-1]==second[j-1]==third[k-1]:
                    answer[k][j][i]=max(answer[k-1][j][i],answer[k][j-1][i],answer[k][j][i-1],answer[k-1][j-1][i],answer[k-1][j][i-1],answer[k][j-1][i-1],answer[k-1][j-1][i-1]+1)
                else:
                    answer[k][j][i]=max(answer[k-1][j][i],answer[k][j-1][i],answer[k][j][i-1],answer[k-1][j-1][i],answer[k-1][j][i-1],answer[k][j-1][i-1],answer[k-1][j-1][i-1])
    # print_answer(answer)
 
    return answer[len(third)][len(second)][len(first)]




if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    # a=[1,2,3]
    # b=[4,5,6]
    # c=[1,3,5]
    print(lcs3(a, b, c))
