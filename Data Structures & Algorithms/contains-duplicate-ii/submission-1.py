class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums) 
        for i in range(n):
            window = nums[i:i+k+1]
            if len(set(window)) != len(window):
                return True
        return False