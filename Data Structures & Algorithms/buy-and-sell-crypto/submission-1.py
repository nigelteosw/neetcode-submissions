class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0
        for i in range(1,n):
            curr = prices[i] - min(prices[:i])
            res = max(res, curr)
        return res