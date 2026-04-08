class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        ppl = sorted(people)
        n = len(people)
        left, right = 0, n - 1
        while left <= right:
            total = ppl[left] + ppl[right]
            if total > limit:
                right -= 1
                res += 1
            else:
                left, right = left + 1, right - 1
                res += 1
        return res