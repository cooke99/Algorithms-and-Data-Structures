def fractional_knapsack(n: int, W: int, costs: list, weights: list) -> float:
    '''
    Greedy algorithm to solve the fractional knapsack problem.
    '''
    
    prices = []
    for i in range(n):
        prices.append(costs[i]/weights[i])
        
    val  = 0
    while((W != 0) and (len(weights) != 0)):
        argmax = max(range(len(prices)), key=prices.__getitem__) # Return index of most valuable compound.
        amount = min(W, weights[argmax]) # The maximum amount we take cannot exceed W or the amount of the compound available.
        val += prices[argmax]*amount
        W -= amount
        # We always pop this item, even if we haven't taken all of it:
        # If we have not taken all of it, the bag is full, and we will
        # stop at the next iteration regardless.
        prices.pop(argmax)
        weights.pop(argmax)
    return val

if __name__=='__main__':
    n, W = list(map(int,input().split()))
    weights = []
    costs = []
    for i in range(n):
        cost, weight = list(map(int,input().split()))
        weights.append(weight)
        costs.append(cost)
    ans = fractional_knapsack(n,W,costs,weights)
    print(ans)
