from sys import stdin


def min_refills(distance, tank, stops):
    # write your code here
    refill=0
    i=1
    capacity=tank
    stops.insert(0,0)
    stops.append(distance)

    while tank<distance:
        #below to handle the edge case when it is not possible to reach the destination
        if stops[i]-stops[i-1]>capacity:
            return -1
        
        if stops[i]>tank:
            tank=stops[i-1]+capacity
            refill+=1
            print(f"Tank Updated:{tank} at: {stops[i-1]}")
        else:
            i+=1
    
    return refill


if __name__ == '__main__':
    # d, m, _, *stops = map(int, stdin.read().split())
    d, m, _, *stops =200,250,2,100,150
    print(min_refills(d, m, stops))
