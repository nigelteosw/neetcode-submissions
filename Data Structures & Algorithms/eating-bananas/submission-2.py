class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        speed = high

        def canEat(speed):
            res = 0
            for p in piles:
                res += (p + speed - 1) // speed
            return res
        
        while low <= high:
            mid = (high + low) // 2
            if canEat(mid) <= h:
                high = mid - 1
                speed = mid
            else:
                low = mid + 1
                
        
        return speed