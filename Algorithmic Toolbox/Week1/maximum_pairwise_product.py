import sys

def maximum_pairwise_product(n, arr):
    max1 = None
    max2 = None

    for i in range(n):
        if ((max1 == None) or (arr[i] > arr[max1])):
            max2 = max1
            max1 = i

        elif ((max2 == None) or (arr[i] > arr[max2])):
            max2 = i

        else:
            continue
    return arr[max1]*arr[max2]

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(maximum_pairwise_product(n,arr))
