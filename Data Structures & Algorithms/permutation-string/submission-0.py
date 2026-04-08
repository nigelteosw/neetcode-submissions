class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        n = len(s1)
        if n > len(s2):
            return False

        for i in range(n):
            s1_count[s1[i]] = 1 + s1_count.get(s1[i], 0)

        for i in range(0, len(s2)-n+1):
            curr = s2[i:i+n]
            s2_window = {}
            for j in range(n):
                s2_window[curr[j]] = 1 + s2_window.get(curr[j], 0)
            if s2_window == s1_count:
                return True

        return False