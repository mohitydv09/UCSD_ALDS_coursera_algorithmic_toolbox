
def fibonacci_fast(num):
    last_num=1
    slast_num=0
    if num<=1:
        return num
    else:
        for i in range(2,num):
            temp_slast=slast_num
            slast_num=last_num
            last_num=last_num+temp_slast
        return last_num+slast_num

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_fast(input_n))