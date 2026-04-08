class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        max_length = 0
        while right < len(s):
            if s[right] not in s[left:right]:
                right += 1
                max_length = max(max_length, right - left)
            else:
                left += 1
                max_length = max(max_length, right - left)
        return max_length