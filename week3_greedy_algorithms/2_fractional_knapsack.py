from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    my_list=[[x/y,x,y] for (x,y) in zip(values,weights)]
    my_list=sorted(my_list,reverse=True)

    i=0
    while capacity:
        if my_list[i][2]:
            quantity_taken=min(capacity,my_list[i][2])
            value+=quantity_taken*my_list[i][0]
            capacity-=quantity_taken
            my_list[i][2]-=quantity_taken
            # print(f"Quantity taken is:{quantity_taken} and value now is:{value}")
        else:
            i+=1
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.6f}".format(opt_value))
