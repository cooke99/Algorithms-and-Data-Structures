import numpy as np

def covering_segments(n: int, L: np.array, R: np.array) -> tuple:
    '''
    Greedy algorithm to find the minimum number of points that
    intersect all (sometimes overlapping) segments along a given line.
    '''
    L_sorted = np.argsort(L) # Sort segments by their starting point.
    L = L[L_sorted]
    R = R[L_sorted]
    k = 0 # Minimum number of intersection points of segments.
    pts = [] # List of intersection points.

    while (len(L) != 0):
        min_R = min(R) # Find the first ending of a segment. All segments that start at or before this point will be intersected by it.
        del_segs = [] # Index of segments to be popped from L and R (the ones that are intersected).
        for seg in range(len(L)):
            # Loop over all segments and check how many
            # are intersected by pt.
            if (L[seg] <= min_R) and (min_R <= R[seg]):
                # If the point intersects this segment
                del_segs.append(seg) # Append this segment index to be popped later.
        k += 1
        pts.append(str(min_R))
        L = np.delete(L, del_segs)
        R = np.delete(R, del_segs)
    
    return k, pts

if __name__=='__main__':
    n = int(input())
    L_arr = [0]*n
    R_arr = [0]*n
    for i in range(n):
        L_arr[i], R_arr[i] = list(map(int,input().split()))

    k, pts = covering_segments(n, np.array(L_arr), np.array(R_arr))
    print(k)
    print(" ".join(pts))
