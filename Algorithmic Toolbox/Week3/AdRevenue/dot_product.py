def dot_product(n: int, prices: list, clicks: list)-> int:
    '''
    Calculate the maximum dot product of prices and clicks
    in a greedy manner: take the product of the largest
    price available and the largest cost available, add
    the result to the running sum, remove this price and
    cost from the list and continue for n-1 iterations.
    '''
    revenue = 0
    for i in range(n):
        argmax_p = max(range(len(prices)), key=prices.__getitem__) # Return index of most valuable price.
        argmax_c = max(range(len(clicks)), key=clicks.__getitem__) # Return index of highest clicks.
        revenue += prices[argmax_p]*clicks[argmax_c]
        prices.pop(argmax_p)
        clicks.pop(argmax_c)
        
    return revenue

if __name__ == '__main__':
    n = int(input())
    prices = list(map(int,input().split()))
    clicks = list(map(int,input().split()))
    ans = dot_product(n,prices,clicks)
    print(ans)
