def print_answer(answer):
    print("Answer:")
    for x in answer:
        print(x)
        
def lcs2(first, second):
    #answer initiallized
    answer=[[0]*(len(second)+1) for _ in range(len(first)+1)]
    # print_answer(answer)
    
    #Any point(i,j can only be reached in the answer only through three channels namely (i-1,j),(i,j-1),(i-1,j-1))
    # We need to go row wise.
    for i in range(1,len(first)+1):
        for j in range(1,len(second)+1):
            # Check for match
            if first[i-1]==second[j-1]:
                answer[i][j]=max(answer[i-1][j],answer[i][j-1],answer[i-1][j-1]+1)
            else:
                answer[i][j]=max(answer[i-1][j],answer[i][j-1],answer[i-1][j-1])
    # print_answer(answer)
    return answer[len(first)][len(second)]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m
    # a=[7,2,9,3,1,5,9,4]
    # b=[2,8,1,3,9,7]
    print(lcs2(a, b))
