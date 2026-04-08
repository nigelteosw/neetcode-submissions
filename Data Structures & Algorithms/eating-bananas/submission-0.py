class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = sum(piles)

        def canFinishIn(piles, k):
            count = 0
            for bananas in piles:
                count += (bananas + k - 1) // k
            return count

        while low <= high:
            mid = low + (high-low)//2
            if canFinishIn(piles, mid) <= h:
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1
        return res