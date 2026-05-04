class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for element in nums:
            res += [current_subset + [element] for current_subset in res]
        return res