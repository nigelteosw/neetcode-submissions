class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for item in strs:
            count = [0] * 26
            for char in item:
                count[ord(char)-ord('a')] += 1

            if tuple(count) not in store.keys():
                store[tuple(count)] = [item]
            else:
                store[tuple(count)].append(item)

        return list(store.values())