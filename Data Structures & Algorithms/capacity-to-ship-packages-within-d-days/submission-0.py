class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        res = high

        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap

                currCap -= w
            return True
        
        while low <= high:
            mid = (high + low) // 2
            if canShip(mid):
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1
        return res