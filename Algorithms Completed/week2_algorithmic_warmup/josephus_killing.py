def j_killing(n,k):
    rebels=[x for x in range(n)]
    i=k-1
    while len(rebels)>1:
        del rebels[i]
        i+=k-1
        if i>=len(rebels):
            i=i-len(rebels)
        print(rebels)

    return rebels[0]

if __name__=='__main__':
    # n,k=map(int,input().split())
    n,k=5,2
    print(j_killing(n,k))