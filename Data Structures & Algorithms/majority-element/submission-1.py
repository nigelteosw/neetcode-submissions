class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        candidate = nums[0]
        if n == 1:
            return candidate
        count = 1
        for i in range(1, n):
            if nums[i] == candidate:
                count += 1
            else:
                if count > 1:
                    count -= 1
                else:
                    candidate = nums[i]
        return candidate