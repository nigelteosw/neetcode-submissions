class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1 and not word2:
            return 
        if not word1 and word2:
            return word2
        if not word2 and word1:
            return word1

        return word1[0] + self.mergeAlternately(word2, word1[1:])