def lcm(a, b):
    return int((a*b)/gcd(a,b))

def gcd(a, b):
    big=max(a,b)
    small=min(a,b)

    if small==0:
        return big
    else:
        new_num=big%small
        return gcd(new_num,small)
        
if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

