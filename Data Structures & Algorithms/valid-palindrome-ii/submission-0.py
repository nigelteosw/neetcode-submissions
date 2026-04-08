class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(n):
            curr = s[i]
            left = s[:i]
            right = s[i+1:]
            temp = left + right
            if self.isPalindrome(temp):
                return True
        return False

    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]