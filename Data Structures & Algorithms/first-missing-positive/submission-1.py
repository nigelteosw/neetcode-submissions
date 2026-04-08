class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr = [0] * (len(nums) + 2)
        for i in range(len(nums)):
            if nums[i] >= 0 and nums[i] < len(nums) + 1:
                arr[nums[i]] += 1
                
        return arr[1:].index(0)+1