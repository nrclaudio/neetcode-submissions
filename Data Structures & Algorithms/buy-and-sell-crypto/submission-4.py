class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        profit = 0
        while R < len(prices):
            if prices[R] < prices[L]:
                L = R
            elif prices[R] > prices[L]:
                profit = max(profit, prices[R] - prices[L])
            R += 1
        return profit
