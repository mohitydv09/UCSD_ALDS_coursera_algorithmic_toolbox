def print_answer(answer):
    print("Answer:")
    for x in answer:
        print(x)

def edit_distance(first_string, second_string):
    # print(first_string,second_string)
    #answer initiallized
    answer=[[0]*(len(first_string)+1) for x in range(len(second_string)+1)]
    # print_answer(answer)
    
    #Fill the answers first row and column as we know there answer.
    answer[0]=[x for x in range(len(first_string)+1)]
    for i in range(len(second_string)+1):
        answer[i][0]=i
    # print_answer(answer)   
     
    #Any point(i,j can only be reached in the answer only through three channels namely (i-1,j),(i,j-1),(i-1,j-1))
    #Go in row
    for i in range(1,len(second_string)+1):
        for j in range(1,len(first_string)+1):
            # For Match condition
            if first_string[j-1]==second_string[i-1]:
                answer[i][j]=min(answer[i-1][j]+1,answer[i][j-1]+1,answer[i-1][j-1])
            else:
                answer[i][j]=min(answer[i-1][j]+1,answer[i][j-1]+1,answer[i-1][j-1]+1)
    
    # print_answer(answer)
    return answer[len(second_string)][len(first_string)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
    # print(edit_distance('ab', 'ab'))