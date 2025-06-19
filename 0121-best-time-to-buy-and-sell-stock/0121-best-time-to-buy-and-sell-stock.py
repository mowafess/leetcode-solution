class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        profit = 0

        for price in prices:
            if price - min_so_far > profit:
                profit = price - min_so_far
            min_so_far = min(price, min_so_far)
        
        return profit