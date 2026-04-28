class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def traverse(count, arr):
            curr = arr
            if count == target:
                res.append(curr)
            elif count <= target:
                for num in nums:
                    traverse(count + num, curr + [num])
            else:
                return False

        traverse(0, [])
        return list(map(list, {tuple(sorted(x)) for x in res}))