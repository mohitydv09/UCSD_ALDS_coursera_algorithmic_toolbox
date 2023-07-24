def change(money,d):
    # write your code here
    count=0
    i=0
    while money:
        if money>=d[i]:
            count+=money//d[i]
            money=money%d[i]
        else:
            i+=1
    return count


if __name__ == '__main__':
    m = int(input())
    d=[10,5,1]
    print(change(m,d))
