class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return -1
        n = len(nums)
        low, high = 0, n
        while low <= high:
            mid = low + (high-low) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1