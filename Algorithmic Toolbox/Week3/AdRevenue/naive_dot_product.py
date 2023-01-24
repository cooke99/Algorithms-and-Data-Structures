import itertools

def naive_dot_product(n: int, prices: list, clicks: list)-> int:
    '''
    Calculate the maximum dot product of prices and clicks
    by iterating through all permutations of clicks and
    returning the largest result.
    '''
    max_revenue = 0

    for permutation in itertools.permutations(clicks):
        # Loop through all permutations of clicks.
        revenue = 0
        for i in range(n):
            revenue += prices[i]*permutation[i]
        max_revenue = max(max_revenue,revenue)
        
    return max_revenue

if __name__ == '__main__':
    n = int(input())
    prices = list(map(int,input().split()))
    clicks = list(map(int,input().split()))
    ans = naive_dot_product(n,prices,clicks)
    print(ans)
