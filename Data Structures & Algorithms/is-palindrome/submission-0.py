class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for i in s:
            if (i.isalnum()):
                arr.append(i.lower())
        n = len(arr)
        for i in range(n//2):
            if arr[i] != arr[-i-1]:
                return False
        return True