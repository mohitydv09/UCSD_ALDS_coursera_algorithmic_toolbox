from sys import stdin

def print_ans(answer):
    print("Answer")
    for x in answer:
        for y in x:
            print(y)
        print('\n')
        
def partition3(weights):
    #Solve the knapsack in two dimentions for two backpacks
    total_sum=sum(weights)
    if total_sum%3!=0:
        return 0
    else:
        capacity=total_sum//3
    answer=[[[0]*(capacity+1) for _ in range(capacity+1)] for _ in range(len(weights)+1)]
    answer[0][0][0]=1
    #Each point P(A,B,i) represents that weather the bag of A capacity and bag of B capacity can be filled with the items till i.
    # Zero elements can fill zero capacity bags therefore P(0,0,0) is 1, and all others are 0

    #Now we start filling for other items
    #At each point for i th item it could be placed in 1st bag or 2 bag or not in any(This is case when it is presetn in third bag).
    #Therefore any point P(A,B,i) can be reached by P(A-w,B,i-1),P(A,B-w,i-1),P(A,B,i-1).
    # If any of the above was true that means we can reach P(A,B,i) by doing one of the above i.e. placing the item in any of the bag.
    # Therefore the algorith is as given below.
    for k in range(1,len(weights)+1):
        weight=weights[k-1]
        for j in range(capacity+1):
            for i in range(capacity+1):
                if j>=weight and i>=weight:
                    if (answer[k-1][j-weight][i]==1 or answer[k-1][j][i-weight]==1 or answer[k-1][j][i]==1):
                        answer[k][j][i]=1
                    else:
                        answer[k][j][i]=0 
                elif j>=weight:
                    if (answer[k-1][j-weight][i]==1 or answer[k-1][j][i]==1):
                        answer[k][j][i]=1 
                    else:
                        answer[k][j][i]=0
                elif i>=weight:
                    if (answer[k-1][j][i-weight]==1 or answer[k-1][j][i]==1):
                        answer[k][j][i]=1
                    else:
                        answer[k][j][i]=0
                else:
                    if answer[k-1][j][i]==1:
                        answer[k][j][i]=1
                    else:
                        answer[k][j][i]=0
        # print("weight:",weight)
        # for x in answer[k]:
        #     print(x)
        # print(answer[k])
    return answer[len(weights)][capacity][capacity]



if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    # input_values=[1,2,3,4,5,5,7,7,8,10,12,19,25]
    # input_values=sorted(input_values,reverse=True)
    # input_values=[1,2,3,4,5,9]
    # input_values=[3,3,3,3,3,3]
    print(partition3(input_values))
