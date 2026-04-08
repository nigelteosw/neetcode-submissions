class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count = 0
        res = len(nums) + 1
        left, right = 0, 0
        while right < len(nums):
            if count >= target:
                res = min(res, right-left+1)
            else:
                count += nums[right]
                right += 1
                while count >= target:
                    count -= nums[left]
                    left += 1
                    res = min(res, right-left+1)

        return res if res <= len(nums) else 0