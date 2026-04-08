class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        for i in range(n-1):
            curr, next = prices[i], prices[i+1]
            if next > curr:
                res += next-curr
        return res