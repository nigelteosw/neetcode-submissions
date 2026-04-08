class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        digits = set(nums)
        res = []
        for i in digits:
            if nums.count(i) > (len(nums)//3):
                res.append(i)
        return res