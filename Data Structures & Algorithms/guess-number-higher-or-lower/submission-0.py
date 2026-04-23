# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, h = 0, n
        while l <= h:
            mid = (l+h)//2
            pick = guess(mid)
            if pick == 0:
                return mid
            if pick == -1:
                h = mid-1
            else:
                l = mid+1