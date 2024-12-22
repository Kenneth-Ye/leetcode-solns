class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 10 1 5 6 7 1
        #  L         R
        # maxProfit = 6
        # curr_profit 6

        max_profit = 0
        lowest = prices[0]
        for price in prices:
            lowest = min(price, lowest)
            max_profit = max(max_profit, price - lowest)
        return max_profit
