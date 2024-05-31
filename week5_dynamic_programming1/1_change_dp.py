def change(money):
    # write your code here
    coins=[1,3,4]
    answer=[0]*(money+1)
    for m in range(1,money+1):
        answer[m]=float('inf')
        #To take the minimum for all the coins
        for i in range(len(coins)):
            if m>=coins[i]:
                num_of_coins=answer[m-coins[i]]+1
                if num_of_coins<answer[m]:
                    answer[m]=num_of_coins
    return answer[money]

if __name__ == '__main__':
    m = int(input())
    print(change(m))
