import itertools
import numpy as np

def powerset(iterable):
    # Python docs recipe
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

def naive_covering_segments(n: int, L: np.array, R: np.array) -> tuple:
    '''
    Naive algorithm to find the minimum number of points that
    intersect all (sometimes overlapping) segments along a given line.
    '''
    start = min(L)
    end =  max(R)
    intersect_pts = dict() # Keys will be numbers on the line, values the list of segments they intersect

    for i in range(start, end+1):
        # Iterate over all points on the line made up by the segments
        intersects = []
        for j in range(n):
            if (L[j] <= i) and (i <= R[j]):
                # If the given segment is intersected by this point, store the index
                intersects.append(j)
        intersect_pts[i] = intersects

    k = n # Number of points of intersection should not be greater than the number of segments
    min_pts = None # Initialise the points of intersection
    for pts in powerset(list(intersect_pts.keys())):
        if len(pts) == 0:
            # Handle null set returned by powerset
            continue
        # We iterate over every possible permutation of points on the line.
        if len(pts) <= k:
            total_segs = [] # Store the indices of the segments intersected by the points in pts.
            for pt in pts:
                total_segs = total_segs + intersect_pts[pt]
                
            if (np.isin(np.array(range(n)),np.array(total_segs))).all():
                # If all segments are intersected by this combination of points
                k = len(pts)
                min_pts = list(map(str,pts))
  
    return k, min_pts

if __name__=='__main__':
    n = int(input())
    L_arr = [0]*n
    R_arr = [0]*n
    for i in range(n):
        L_arr[i], R_arr[i] = list(map(int,input().split()))

    k, pts = naive_covering_segments(n, np.array(L_arr), np.array(R_arr))
    print(k)
    print(" ".join(pts))
