def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def print_ans(matrix):
    for x in matrix:
        print(x)

def minandmax(dataset,maxi,mini,i,j):
    max_return=float('-inf')
    min_return=float('inf')
    for k in range(i,j):
        max_k=int(maxi[i-1][k-1])
        min_k=int(mini[i-1][k-1])
        max_k1=int(maxi[k][j-1])
        min_k1=int(mini[k][j-1])
        opr=dataset[(2*(k-1))+1]
        max_return_temp=max(evaluate(max_k,max_k1,opr),evaluate(max_k,min_k1,opr),evaluate(min_k,max_k1,opr),evaluate(min_k,min_k1,opr))
        min_return_temp=min(evaluate(max_k,max_k1,opr),evaluate(max_k,min_k1,opr),evaluate(min_k,max_k1,opr),evaluate(min_k,min_k1,opr))
        if max_return<max_return_temp:
            max_return=max_return_temp
        if min_return_temp<min_return:
            min_return=min_return_temp
    return max_return,min_return

def maximum_value(dataset):
    # write your code here
    n=(len(dataset)//2) +1

    #Initiate the matrix to hold the values
    #Minimim Matrix
    mini=[[0]*n for _ in range(n)]
    #Maximum Matrix
    maxi=[[0]*n for _ in range(n)]
    
    #Fill the matrix for diagonal values
    for i in range(n):
        mini[i][i]=dataset[2*i]
        maxi[i][i]=dataset[2*i]

    for s in range(1,n):
        for i in range(1,n-s+1):
            j=i+s
            maxi_ele,mini_ele=minandmax(dataset,maxi,mini,i,j)
            maxi[i-1][j-1]=maxi_ele
            mini[i-1][j-1]=mini_ele
            # print('Maximum:')
            # print_ans(maxi)
            # print('Minimum:')
            # print_ans(mini)
    return maxi[0][n-1]


if __name__ == "__main__":
    print(maximum_value(input()))
    # print(maximum_value('5-8+7*4-8+9'))
