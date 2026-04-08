class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, currSum = 0, 0
        hashmap = { 0:1 }
        
        for num in nums:
            currSum += num
            diff = currSum - k
            
            res += hashmap.get(diff, 0)
            hashmap[currSum] = 1 + hashmap.get(currSum, 0)
            
        return res