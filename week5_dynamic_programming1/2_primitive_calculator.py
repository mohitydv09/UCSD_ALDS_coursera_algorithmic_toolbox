def compute_operations(n):
    answer=[0]*(n+1)
    
    for i in range(2,n+1):
        prefix=[float(i-1),i/2,i/3]
        values_at_prefix=[answer[int(x)] if x.is_integer() else float('inf') for x in prefix]
        answer[i]=min(values_at_prefix)+1
    # print(f"Answers:{answer}")
    
    steps=[n]
    while n>1:
        if answer[n]==answer[n-1]+1:
            steps.append(n-1)
            n=n-1
            # print(f"+1 was last step")
            # print(steps)
        if answer[n]==answer[n//2]+1:
            if (n/2).is_integer():
                steps.append(int(n/2))
                n=int(n/2)
                # print(steps)
        if answer[n]==answer[n//3]+1:
            if (n/3).is_integer():
                steps.append(int(n/3))
                n=int(n/3)
                # print(steps)
    return steps[::-1]

if __name__ == '__main__':
    input_n = int(input())
    # input_n=1
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
