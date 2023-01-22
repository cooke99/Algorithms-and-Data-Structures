import itertools

def naive_fractional_knapsack(n: int, W: int, costs: list, weights: list) -> float:
    '''
    Naive implementation to solve fractional knapsack
    problem. Tests all combinations of n compounds
    and returns the one with largest value. Only tests
    integer weights of compounds for simplicity (and speed).
    This should be ok as the inputs are all ints.
    '''
    if (W == 0):
        return 0
    
    prices = []
    all_weight_vals = [] # List to store all possible integer values of weights[i] for each n compounds.
    for i in range(n):
        prices.append(costs[i]/weights[i])
        all_weight_vals.append(list(range(weights[i]+1)))
    # Generate all possible permutations of the n weights:
    perms = list(itertools.product(*all_weight_vals))
    max_val = 0 # Store best value found so far.
    for permutation in perms:
        if (sum(permutation) > W):
            # If the total weight of this permutation exceeds W
            continue # Skip it
        else:
            val = 0
            for j in range(n):
                val += prices[j]*permutation[j]
            max_val = max(val,max_val)
            
    return max_val

if __name__=='__main__':
    n, W = list(map(int,input().split()))
    weights = []
    costs = []
    for i in range(n):
        cost, weight = list(map(int,input().split()))
        weights.append(weight)
        costs.append(cost)
    ans = naive_fractional_knapsack(n,W,costs,weights)
    print(ans)
