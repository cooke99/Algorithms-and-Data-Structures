import itertools
import numpy as np

def powerset(iterable):
    # Python docs recipe
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

def naive_car_fueling(d: int, m: int, n: int, stops: list) -> int:
    '''
    Naive implementation to solve car fueling
    problem. Tests all combinations of stops
    and returns the one with minimum number of
    stops that can reach the destination.
    '''
    if (m >= d):
        # If we can travel the distance d without stopping.
        return 0

    elif ((stops[0] > m) or any(np.diff(stops) > m) or (d - stops[-1] > m)):
        # If the distance between 2 successive stops
        # is greater than m, the trip cannot be completed.
        return -1

    else:
        min_stops = n
        for stop_seq in powerset(stops):
            # Loop through all possible combinations of stops.
            stop_seq = list(stop_seq)
            stop_seq.append(d) # City2 is technically the last stop.
            if ((stop_seq[0] > m) or any(np.diff(stop_seq) > m)):
                # If this permutation of stops cannot be reached.
                continue
            else:
                # If we can reach city2 with this sequence of stops:
                min_stops = min(min_stops, len(stop_seq)-1)
        return min_stops

if __name__=='__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int,input().split()))
    ans = naive_car_fueling(d, m, n, stops)
    print(ans)
