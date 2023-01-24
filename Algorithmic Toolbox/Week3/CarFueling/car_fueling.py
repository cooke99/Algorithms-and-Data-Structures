import numpy as np

def car_fueling(d: int, m: int, n: int, stops: list) -> int:
    if (d <= m):
        # If we can reach city2 from our current location without stopping.
        return 0
    
    elif ((len(stops) == 0) or(stops[0] > m) or any(np.diff(stops) > m) or (d - stops[-1] > m)):
        # If the distance between 2 successive stops
        # is greater than m, the trip cannot be completed.
        return -1

    else:
        stops = np.array(stops)
        # Find the index of the furthest stop we can get to on 1 tank of fuel.
        furthest_stop_idx = np.where(stops <= m)[0][-1] 
        furthest_stop = stops[furthest_stop_idx] # Find the distance to this stop.
        stops = stops - furthest_stop # Update distance to stops with new location.
        stops = stops[furthest_stop_idx+1:] # We remove all stops up to and including the latest stop for the next recursive call.
        return 1 + car_fueling(d - furthest_stop, m, n, stops)

if __name__=='__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int,input().split()))
    ans = car_fueling(d, m, n, stops)
    print(ans)
