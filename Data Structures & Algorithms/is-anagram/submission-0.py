class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp1 = {}
        temp2 = {}
        for i in s:
            if i in temp1:
                temp1[i] += 1
            else:
                temp1[i] = 1
        for i in t:
            if i in temp2:
                temp2[i] += 1
            else:
                temp2[i] = 1
        return temp1 == temp2