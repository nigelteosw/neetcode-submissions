class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        mid = n//2
        pivot = nums[mid]
        left = []
        middle = []
        right = []
        for i in range(n):
            if nums[i] < pivot:
                left.append(nums[i])
            elif nums[i] == pivot:
                middle.append(nums[i])
            else:
                right.append(nums[i])
        return self.sortArray(left) + middle + self.sortArray(right)