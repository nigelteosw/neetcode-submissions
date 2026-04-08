class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted_nums = sorted(nums)
        n = len(sorted_nums)

        for i in range(n - 2):
            # Skip duplicates for i
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])

                    # Skip duplicates for left and right
                    while left < right and sorted_nums[left] == sorted_nums[left + 1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return res