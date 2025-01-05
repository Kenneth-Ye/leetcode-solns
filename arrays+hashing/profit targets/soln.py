def stockPairs(stocksProfit, target):
    # Write your code here
    seen = {} # num: true/false
    pairs = 0
    for price in stocksProfit:
        if target - price in seen:
            if not seen[target - price]:
                seen[target - price] = True
                pairs += 1
            else:
                continue
        else:
            seen[price] = False
    return pairs